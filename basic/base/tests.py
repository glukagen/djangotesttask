from django.test import Client, TestCase
from base.models import Location, Person, Log
from django.template import Context, Template
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.db.models.loading import get_models
import sys
import os


class SimpleTest(TestCase):
    fixtures = ['initial_data.json']
    password = 'password'
    username = 'name'

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(self.username, 'tt@tt.com', \
                                             self.password)
        self.user.is_staff = True
        self.user.save()

    def login(self):
        login = self.client.login(username=self.username, \
                                  password=self.password)
        self.failUnless(login, 'Could not log in')

    def test_signals(self):
        count = Log.objects.count()
        p = Person(name=self.username, date='2010-10-10')
        p.save()
        self.failUnlessEqual(count + 1, Log.objects.count())
        p.delete()
        self.failUnlessEqual(count + 2, Log.objects.count())

    def test_firstpage(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/login')

        self.login()
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        p = Person.objects.get(pk=1)
        self.assertContains(response, p.name)
        self.assertContains(response, p.surname)
        self.assertContains(response, p.bio)
        self.assertContains(response, p.contacts)

    def test_middleware(self):
        self.login()
        count = Location.objects.count()
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(count + 1, Location.objects.count())

    def test_settings(self):
        self.login()
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(response.context['settings'], settings)

    def test_form_person_save(self):
        data = {
            'name': 'test_name',
            'surname': 'test_surname',
            'bio': 'test_bio',
            'contacts': 'test_contacts',
            'date': '2010-10-10',
        }

        response = self.client.post('/save_person', data)
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(response.content, 'You are not authorized')

        self.login()
        response = self.client.post('/save_person', data)
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(response.content, '1')

        p = Person.objects.get(pk=1)
        self.failUnlessEqual(data['name'], p.name)
        self.failUnlessEqual(data['surname'], p.surname)
        self.failUnlessEqual(data['bio'], p.bio)
        self.failUnlessEqual(data['contacts'], p.contacts)

    def test_list_middleware(self):
        response = self.client.get('/middleware')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'First 10 http requests:')
        for loc in Location.objects.all()[:10]:
            self.assertContains(response, loc)

    def test_tag(self):
        response = Template("{% load mytag %}{% get_url user %}").render(
            Context({"user": self.user}))
        c = self.user.__class__
        self.failUnlessEqual(response, reverse('admin:%s_%s_change' %  \
            (c._meta.app_label, c._meta.module_name), args=[self.user.pk]))

    def test_command(self):
        sys.stdout = open('dump_mycommand.txt', 'w')
        call_command('mycommand')
        sys.stdout.close()
        sys.stdout = sys.__stdout__

        f = file('dump_mycommand.txt', "r")
        result = "Project models:\n%s" % \
            "\n".join(["%s - %s" % (m._meta.object_name, m.objects.count())
                         for m in get_models()])
        self.failUnlessEqual(f.read().strip('\n'), result.strip('\n'))
        f.close()
        os.remove('dump_mycommand.txt')

from django.test import Client, TestCase
from base.models import Location, Person
from django.template import Context, loader
from django.http import HttpResponse
from django.conf import settings

class SimpleTest(TestCase):
    fixtures = ['base.json']

    def setUp(self):
        self.client = Client()

    def test_firstpage(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        
    def test_middleware(self):
        count = Location.objects.count()
        response = self.client.get('/')
        self.failUnlessEqual(count+1, Location.objects.count())    

    def test_settings(self):
        response = self.client.get('/settings')
        self.failUnlessEqual(response.status_code, 200)            
        self.failUnlessEqual(response.content,
            loader.get_template('settings.html').render(Context(
                {'settings': settings,})))
        
    def test_form_person_save(self):
        data = {
            'name': 'test_name',
            'surname' : 'test_surname',
            'bio' : 'test_bio',
            'contacts' : 'test_contacts'
        }
        
        response = self.client.post('/', data)
        self.failUnlessEqual(response.status_code, 200)
        
        p = Person.objects.get(pk=1)
        self.failUnlessEqual(data['name'], p.name)
        self.failUnlessEqual(data['surname'], p.surname)
        self.failUnlessEqual(data['bio'], p.bio)
        self.failUnlessEqual(data['contacts'], p.contacts)    


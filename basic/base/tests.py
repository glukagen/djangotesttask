from django.test import Client, TestCase
from base.models import Location
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


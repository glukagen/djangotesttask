from django.test import Client, TestCase

class SimpleTest(TestCase):
    fixtures = ['base.json']

    def setUp(self):
        self.client = Client()

    def test_firstpage(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

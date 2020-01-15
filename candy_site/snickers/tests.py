from django.test import SimpleTestCase
from django.urls import reverse

class SnickersTest(SimpleTestCase):

    def test_home_page(self):
        url = reverse('home')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'links.html')

    
    def test_about_snickers_template(self):
        url = reverse('about_snickers')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about_snickers.html')
        self.assertTemplateUsed(response, 'links.html')

from django.test import TestCase


class TestView(TestCase):

    def test_that_home_loads(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/home.html')

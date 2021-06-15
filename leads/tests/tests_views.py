from django.test import TestCase
from django.shortcuts import reverse
# Django executes all functions in class that start with test as a single test


class LandingPageTest(TestCase):

    def test_get(self):
        # send request to landing page
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

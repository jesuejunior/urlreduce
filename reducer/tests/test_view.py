from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class ReviewViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="jj", email='tests@jesuejunior.com')
        self.user.set_password('tests123')
        self.user.save()

        self.client.login(username=self.user.username, password='tests123')


    def test_access_home(self):
        """
        Test to get response correct with reverse url, it's test a url/view
        """
        response = self.client.get(reverse('reduce:home'))

        self.assertEquals(response.status_code, 200)

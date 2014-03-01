from unittest import TestCase
from django.contrib.auth.models import User
from django.db import models
from reducer.models import Link, Owner


class LinkModelTest(TestCase):

        def test_url_hash(self):
            link = Link._meta.get_field_by_name('url_hash')[0]
            self.assertEquals(link.__class__, models.CharField)
            self.assertEquals(link.max_length, 255)
            self.assertTrue(link.null)
            self.assertTrue(link.blank)
            self.assertTrue(link.unique)

        def test_user(self):
            link = Link._meta.get_field_by_name('user')[0]
            self.assertEquals(link.__class__, models.ForeignKey)

        def test_url(self):
            link = Link._meta.get_field_by_name('url')[0]
            self.assertEquals(link.__class__, models.URLField)

        def test_dt_created(self):
            link = Link._meta.get_field_by_name('dt_created')[0]
            self.assertEquals(link.__class__, models.DateTimeField)
            self.assertTrue(link.auto_now_add)

class OwnerModelTest(TestCase):
    def test_link(self):
        owner = Owner._meta.get_field_by_name('link')[0]
        self.assertEquals(owner.__class__, models.ForeignKey)

    def test_owners(self):
        owner = Owner._meta.get_field_by_name('link')[0]
        self.assertEquals(owner.__class__, models.ForeignKey)

class UseruModelTest(TestCase):
    def test_username(self):
        user = User._meta.get_field_by_name('username')[0]
        self.assertEquals(user.max_length, 30)
        self.assertTrue(user.unique)
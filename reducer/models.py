from django.contrib.auth.models import User
from django.db import models
import base64
import hashlib


class LinkManager(models.Manager):

    def encode(self, url):
        hasher = hashlib.sha1(url)
        return base64.urlsafe_b64encode(hasher.digest()[0:4])

    def decode(self, hash):
        return self.get(url_hash=hash).url

class Link(models.Model):
    url_hash = models.CharField(max_length=255, blank=True, null=True, unique=True)
    url = models.URLField()
    dt_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    objects = LinkManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.url_hash = self.get_hash
        super(Link, self).save(force_insert, force_update, using, update_fields)


    @property
    def get_hash(self):
        return Link.objects.encode(self.url)

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'dt_created': self.dt_created,
            'url_hash': self.url_hash,
            'user': self.user.username if self.user else None

        }

    def __unicode__(self):
        return self.url

#nao implementada
class Owner(models.Model):
    link = models.ForeignKey(Link)
    owners = models.ManyToManyField(User, related_name='owners', db_table='owner_has_link', null=True, blank=True)
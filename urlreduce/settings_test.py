# -*- coding: utf-8 -*-
__author__ = 'jesuejunior'
from urlreduce.settings import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': "::memory::",
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append(
    'django_nose'
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
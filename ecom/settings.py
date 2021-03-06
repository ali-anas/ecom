"""
Django settings for ecom project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'stdo#&i)4-(ordm^a(tj&!sm_*5nzjh*vm)8%m=y*9#&6dqncy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# firebase
FIREBASE_ORM_CERTIFICATE = 'static\protean-sensor-278302-firebase-adminsdk-c67u8-e63e2fd2dc.json'
# FIREBASE_ORM_BUCKET_NAME = '<BUCKET_NAME>.appspot.com'
# new
# from pyrebase import pyrebase
# # default_app = firebase_admin.initialize_app()
# config = {
#     "apiKey": "AIzaSyB2dcKOFsNIcAc0yOGAvMaNCcaVRYe4Fq8",
#     "authDomain": "protean-sensor-278302.firebaseapp.com",
#     "databaseURL": "my_firebase_database_url_is_here",
#     "projectId": "protean-sensor-278302",
#     "storageBucket": "protean-sensor-278302.appspot.com",
#     "serviceAccount": "static\protean-sensor-278302-firebase-adminsdk-c67u8-e63e2fd2dc.json",
#     "messagingSenderId": "111376756390"
# }
# # 
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# cred = credentials.Certificate("static\protean-sensor-278302-firebase-adminsdk-c67u8-e63e2fd2dc.json")
# firebase_admin.initialize_app(cred)
# config = {

#     apiKey: "AIzaSyB2dcKOFsNIcAc0yOGAvMaNCcaVRYe4Fq8",
#     authDomain: "protean-sensor-278302.firebaseapp.com",
#     projectId: "protean-sensor-278302",
#     storageBucket: "protean-sensor-278302.appspot.com",
#     messagingSenderId: "111376756390",
#     appId: "1:111376756390:web:c1cc411fd7c8b45e6b4e67",
#     measurementId: "G-HY0JP1SN5F"
# }
# initialize app with config
# firebase = pyrebase.initialize_app(config)

# authenticate a user
# auth = firebase.auth()
# user = auth.sign_in_with_email_and_password("email@usedforauthentication.com", "FstrongPasswordHere")


# db = firebase.database()
# firebase
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'ecom_home.apps.EcomHomeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # alauth
    'django.contrib.sites',
    # 'bootstrapform',
    'crispy_forms',
    # 'allauth_bootstrap',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework'
    # 'cart_template_tags',
    # alauth
    # color 

    # 'colorfield' 
]
SITE_ID = 1


LOGIN_REDIRECT_URL = '/'
# STRIPE_PUBLIC_KEY = config('pk_test_51Hei18AlscERxMKmLir2ST5nttbBanqfNmv4sinecEx8xlehYTa4DQhi4xwjsHKW9ytXQqHOpYmXXFkZIuEkvXYE00fbEYoJWQ')
# STRIPE_SECRET_KEY = config('sk_test_51Hei18AlscERxMKmZLBAS2kh7kQuisaZqYxGI8ukH5YLeochFMiMDtPqT17yumgNCLOfaA4ZSdjRgktZcoSl41PY00oBbqAe82')
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['TEMPLATES'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'from django.template.context_processors.media',
                

            ],
        },
    },
]



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = 'ecom.wsgi.application'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# date

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR,'static' , "live-static", "static-root")
# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
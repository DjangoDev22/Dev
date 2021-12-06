import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#3!$c$^u=x8d=(&^j&ua=ajbn74@p@irm)181o+0k-b9t6e$3-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Applications definition
DJANGO_APPS= [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize'
]
MY_APPS= [
    'home.apps.HomeConfig',
    'comments.apps.CommentsConfig',
    'posts.apps.PostsConfig',
    'users.apps.UsersConfig',
    'newsletter.apps.NewsletterConfig',
]
THIRD_PARTY_APPS= [
    'rest_framework',
    'django_social_share',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
]

INSTALLED_APPS= DJANGO_APPS + MY_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'project/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'project/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (Uploaded Images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Django allauth
LOGIN_REDIRECT_URL= "home"
LOGOUT_REDIRECT_URL= "user_login"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',                                 # login by username and password.
    'allauth.account.auth_backends.AuthenticationBackend'                        # login by social websites as allauth
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
}

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'

# send mail
EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER= 'OmarKhalafJunior2021@gmail.com'
EMAIL_HOST_PASSWORD= 'nxedvdiucflgxikg'
EMAIL_PORT= 587
EMAIL_USE_TLS= True
EMAIL_USE_SSL= False


# client id >> 54288931476-4tn45e95f3tbhclf6kal6as7tc739rqi.apps.googleusercontent.com
# client secret >> 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

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# username >> blogAdmin
# password >> 12052000

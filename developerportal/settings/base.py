"""
Django settings for developerportal project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from django.core.management.utils import get_random_secret_key

from wagtail.embeds.oembed_providers import all_providers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", get_random_secret_key())


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# Application definition
INSTALLED_APPS = [
    "developerportal.apps.common",
    "developerportal.apps.articles",
    "developerportal.apps.content",
    "developerportal.apps.events",
    "developerportal.apps.externalcontent",
    "developerportal.apps.health",
    "developerportal.apps.home",
    "developerportal.apps.mozimages",
    "developerportal.apps.people",
    "developerportal.apps.staticbuild",
    "developerportal.apps.topics",
    "developerportal.apps.videos",
    "wagtail.contrib.forms",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "storages",
    "bakery",
    "wagtailbakery",
    "modelcluster",
    "taggit",
    "social_django",
    "django_countries",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_results",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "wagtail.core.middleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "developerportal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                "developerportal.context_processors.directory_pages",
                "developerportal.context_processors.google_analytics",
                "developerportal.context_processors.mapbox_access_token",
            ],
            "libraries": {
                "app_filters": "developerportal.templatetags.app_filters",
                "app_tags": "developerportal.templatetags.app_tags",
            },
        },
    }
]

AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

WSGI_APPLICATION = "developerportal.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        )
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Email setup
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS", True))
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    ("css", os.path.join(BASE_DIR, "dist/css")),
    ("js", os.path.join(BASE_DIR, "dist/js")),
    ("fonts", os.path.join(BASE_DIR, "src/fonts")),
    ("img", os.path.join(BASE_DIR, "src/img")),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# Django security settings (see `manage.py check --deploy`)

CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SECURE_SSL_REDIRECT = bool(os.environ.get("SECURE_SSL_REDIRECT", False))
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"

# Wagtail settings

WAGTAIL_SITE_NAME = "Mozilla Developer"

# Add support for CodePen oEmbed
WAGTAILEMBEDS_FINDERS = [
    {
        "class": "wagtail.embeds.finders.oembed",
        "providers": all_providers
        + [
            {
                "endpoint": "http://codepen.io/api/oembed",
                "urls": ["^http(?:s)?://codepen\\.io/.+/pen/.+$"],
            }
        ],
    }
]

WAGTAILIMAGES_IMAGE_MODEL = "mozimages.MozImage"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = os.environ.get("BASE_URL")


# Wagtail Bakery Settings

# This is a handy default for local building, but note that when we build in production
# we're actually using this as a root of a build path, to prevent concurrent builds
# from clashing.
BUILD_DIR = os.path.join(BASE_DIR, "build")

BAKERY_MULTISITE = True
BAKERY_VIEWS = (
    # The order of these views is significant - we need CloudfrontInvalidationView
    # to run last of all
    "developerportal.apps.bakery.views.AllPublishedPagesViewAllowingSecureRedirect",
    "bakery.views.Buildable404View",
    "developerportal.apps.bakery.views.S3RedirectManagementView",
    "developerportal.apps.bakery.views.CloudfrontInvalidationView",
)
AWS_REGION = os.environ.get("AWS_REGION")

# This bucket is where the static site will be baked to
AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# This bucket is where user-media will be uploaded to
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_DEFAULT_ACL = "public-read"

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# This is critical for django-bakery NOT to try to do a filesystem copy on a URI in S3
MEDIA_ROOT = None

# Explicit configuration of where the 'baked' site will end up. This needs to match
# the root URL of the developerportal Site in Wagtail's configuration, because
# THAT value (Site.hostname) is what determines the domain used in any absolute
# URLs generated.
# However, we need to also have that root URL available here, because we must add it to
# ALLOWED_HOSTS, else we will hit `DisallowedHost:Invalid HTTP_HOST header` during
# baking in production mode, which then outputs all pages saying "400 Bad Request".

EXPORTED_SITE_URL = os.environ.get("EXPORTED_SITE_URL")  # eg https://example.net

# Static build management commands called in order
STATIC_BUILD_PIPELINE = (("Build", "build"), ("Publish", "publish"))

# Amazon S3 config
S3_BUCKET = os.environ.get("S3_BUCKET")
AWS_CLOUDFRONT_DISTRIBUTION_ID = os.environ.get("AWS_CLOUDFRONT_DISTRIBUTION_ID")

# Social Auth pipelines
SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "developerportal.pipeline.github_user_allowed",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.mail.mail_validation",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
    "developerportal.pipeline.success_message",
)

# GitHub scope to check emails and correct domains
SOCIAL_AUTH_GITHUB_SCOPE = ["user:email"]

# GitHub social auth access keys
SOCIAL_AUTH_GITHUB_KEY = os.environ.get("GITHUB_CLIENT_ID")
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get("GITHUB_CLIENT_SECRET")

LOGIN_ERROR_URL = "/admin/"
LOGIN_REDIRECT_URL = "/admin/"
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/admin/login/"

# GOOGLE_ANALYTICS
GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS")

# Mapbox
MAPBOX_ACCESS_TOKEN = os.environ.get("MAPBOX_ACCESS_TOKEN")

COUNTRIES_FIRST = ["US", "GB"]

# Celery settings
CELERY_BROKER_URL = os.environ.get("REDIS_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = "django-db"  #  for django-celery-results
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

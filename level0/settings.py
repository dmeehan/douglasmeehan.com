# Django settings for level0 project.

import os.path

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dmeehan', 'dmeehan@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media", "uploads")
MEDIA_URL = "/media/uploads/"

STATIC_ROOT = os.path.join(PROJECT_ROOT, "media", "static")
STATIC_URL = "/media/static/"

STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a&c_d0kvgoe7ux-o0edn*#%ui)m1vfh)c3)tlzmzxnx^qrmg21'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader"
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware"
]

ROOT_URLCONF = 'level0.urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.staticfiles',
      
    #admin
    #'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    
    # third party
    'debug_toolbar',
    'tagging',
    'imagekit',
    
    # local
    'level0.contacts',
    'level0.media',
    'level0.portfolio',
)

INTERNAL_IPS = ('67.18.189.122', '127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
	    'INTERCEPT_REDIRECTS': False,
	}

# Setting for the 'Posts' app

POSTS_MARKUP = 'wsywig'

# Settings for comments

COMMENTS_MODERATE_AFTER = 30
COMMENTS_CLOSE_AFTER = 30

# Setting for imageKit

PHOTOLOGUE_MAXBLOCK =  1024 * 2 ** 10 


#==============================================================================
# local environment settings
#==============================================================================

try:
    from local_settings import *
except ImportError:
    pass

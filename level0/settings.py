# Django settings for level0 project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dmeehan', 'dmeehan@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'dmeehan'             # Or path to database file if using sqlite3.
DATABASE_USER = 'dmeehan'             # Not used with sqlite3.
DATABASE_PASSWORD = 'bblmag2e'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

EMAIL_HOST_USER = 'dmeehan'
EMAIL_HOST_PASSWORD = 'bblmag2e'
EMAIL_HOST = 'http://smtp.webfaction.com'
EMAIL_PORT = ''
DEFAULT_FROM_EMAIL = 'admin@level0design.com'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/dmeehan/webapps/level0_media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://www.douglasmeehan.com/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/grappelli/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a&c_d0kvgoe7ux-o0edn*#%ui)m1vfh)c3)tlzmzxnx^qrmg21'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'level0.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/dmeehan/webapps/level0_django/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.markup',
      
    #admin
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    
    # third party
    'debug_toolbar',
    'tagging',
    'imagekit',
    'basic.inlines',
    'basic.blog',    
    
    # local
    'level0.contacts',
    'level0.media',
    'level0.portfolio',
    'level0.posts',
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

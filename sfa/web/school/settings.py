import os
from django.urls import reverse_lazy


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT

PRODUCTION_SETTING = False

if PRODUCTION_SETTING:

    DEBUG = False
    PRODUCTION = True
    USE_PG_IN_DEBUG = True


else:

    DEBUG = True 
    PRODUCTION = False
    USE_PG_IN_DEBUG = False    

if PRODUCTION:
    SECRET_KEY = os.environ['SECRET_KEY']
else: 
    SECRET_KEY = '+NJdG(42e)Y3=@ocYLUJy%MshbsaLrP&o}7go3H4984,8xeuc;'

if DEBUG:
    if USE_PG_IN_DEBUG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ['DB_NAME'],
                'USER': os.environ['DB_USER'],
                'PASSWORD': os.environ['DB_PASS'],
                'HOST': os.environ['DB_SERVICE'],
                'PORT': os.environ['DB_PORT']
            } 
        }
    else:    
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
else: 
    if USE_PG_IN_DEBUG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ['DB_NAME'],
                'USER': os.environ['DB_USER'],
                'PASSWORD': os.environ['DB_PASS'],
                'HOST': os.environ['DB_SERVICE'],
                'PORT': os.environ['DB_PORT']
            } 
        }
    else:    
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }


ALLOWED_HOSTS = [
    "localhost",
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Asia/Singapore"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


if PRODUCTION:
    STATIC_ROOT = "/www/static"
else:   
    STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")
    
# static files dirs use for local pointer of additional static files 

if not os.path.exists('static'):
    os.makedirs('static')

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT,"static", "dist"),
]

STATIC_URL = "/site_media/static/"

if PRODUCTION:
    MEDIA_ROOT = "/www/site_media/media"
else:
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

MEDIA_URL = "/site_media/media/"


STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "account.context_processors.account",
                "school.context_processors.settings"
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "school.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "school.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    # templates
    "bootstrapform",
    "pinax.templates",

    # external
    "account",
    "pinax.eventlog",
    "pinax.webanalytics",
    "import_export",
    'constance',
    'constance.backends.database',

    # project
    "school",
    "attendance",
]

ADMIN_URL = "admin:index"
CONTACT_EMAIL = "support@example.com"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]


ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_LOGIN_REDIRECT_URL = "/attendance/home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True

AUTHENTICATION_BACKENDS = [
    "account.auth_backends.UsernameAuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]


if PRODUCTION:
    # ANYMAIL = {
    #     "MAILGUN_API_KEY": "0e69387c261881681ff77c376d7ec2a2-8b7bf2f1-ff8fa50d",
    #     "MAILGUN_SENDER_DOMAIN": 'mg.demure-kw.com',  # your Mailgun domain, if needed
    # }
    # EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend" 

    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

   
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_FROM_EMAIL = "SFA <no-reply@sfa.com>"  
SERVER_EMAIL = "SFA <error@sfa.com>"
ADMINS = [('Jr','crimsonfierce4@gmail.com'),]

if PRODUCTION:
    LOG_DIR = "/www"
else:
    LOG_DIR =  PROJECT_ROOT
    if not os.path.exists(PROJECT_ROOT+"/logs"):
        os.makedirs(PROJECT_ROOT+"/logs")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "filters": {
        "require_debug_false": { # Run Debug in production
            "()": "django.utils.log.RequireDebugFalse"
        },
        'require_debug_true': { # Do not run debug logger in production
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
	        'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
	        'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR +  '/logs/ecommerce_log.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },  
    
        "mail_admins": { # Error logging by sending email to mail admins when 500 error occured
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
       
        "django.request": { # Logging error occured in django request returning 500 error
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

# ssl settings
# if PRODUCTION:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#     # to ensure that cookies and data are only being send over https connections.
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True


# Debug
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar',]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    INTERNAL_IPS = "127.0.0.1, 192.168.1.21, localhost, 192.168.8.121"


CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {

    'TWILIO_IS_ACTIVE': (True, "Activate twilio"),
    'TWILIO_ACCOUNT_SID': ("AC417cbde6de0611b62a14f91ad3341a92", "Twilio account SID."),
    'TWILIO_AUTH_TOKEN': ("61d78d30e045c218b0482a6b2f1a46a0", "Twilio auth token."),
    'TWILIO_DEFAULT_CALLERID': ("+15406845863", "Twilio Phone number")
}


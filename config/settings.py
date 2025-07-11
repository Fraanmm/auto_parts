from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-x$k#%fnnj@*(+j_0w72q-57y$xni)#n6g!zv1gdah*6y-vpqzd'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tienda',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'tienda' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autoparts',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'tienda' / 'static']

# Transbank (Webpay) - Modo test
TRANSBANK_COMMERCE_CODE = '597055555532'
TRANSBANK_API_KEY = '597055555532'

CSRF_TRUSTED_ORIGINS = [
    "https://webpay3g.transbank.cl",
    "https://webpay3gint.transbank.cl",
    "https://webpay3g-test.transbank.cl",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# Chilexpress API - Configuración completa
CHILEXPRESS_BASE_URL = "http://testservices.wschilexpress.com"

CHILEXPRESS_API_KEYS = {
    'cobertura': {
        'PRIMARY': '782c134e544d425ebee52f49da58ed44',
        'SECONDARY': '03bd3842da1e4082a6d1f33d81149214',
    },
    'cotizador': {
        'PRIMARY': '8bceb0c7f1e4448a9980a5047447285e',
        'SECONDARY': '9d06ee2a25a942408763135d468bff00',
    },
    'envio': {
        'PRIMARY': '714a58fde6d74af99b4987dae288ce31',
        'SECONDARY': 'cbe360f2b528486cb8e051af9dcaa393',
    },
    'georeference': {
        'PRIMARY': '15e4d99f034146bba3157d656f1c836d',
        'SECONDARY': 'bf05d87986804fc0af1205759adb6cd6',
    }
}

CHILEXPRESS_CLIENT_EMAIL = 'franciscaortegaurzua@gmail.com'


from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
ROOT_URLCONF = 'gemini_project.urls'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'

# Session Settings
SESSION_ENGINE = "django.contrib.sessions.backends.db"

SECRET_KEY = '4h^b+7$nv47q2d6=_#1m_s0ggffpr!7u@o6t56&+u%=cm4svo@'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatbot',  # Chatbot app
]

DEBUG = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Ensure this is before AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add your template directory here
        'APP_DIRS': True,  # Ensures app templates are also used
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to your SQLite database file
    }
}

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'https://localhost:8000',  # If you're using HTTPS
]

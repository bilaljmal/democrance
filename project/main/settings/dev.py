import os

from .base import *


AUTH_USER_MODEL = "accounts.Users"

if DEBUG==True:
    DJANGO_DB_HOST='localhost'
    DJANGO_DB_NAME='neksio_dev'
    DJANGO_DB_USER='neksio'
    DJANGO_DB_PASSWORD='*Beejay123qweasd'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DJANGO_DB_NAME,
            'USER': DJANGO_DB_USER,
            'PASSWORD': DJANGO_DB_PASSWORD,
            'HOST': DJANGO_DB_HOST,
            'PORT': 5432,
        }
    }
    # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # SECURE_SSL_REDIRECT = True
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True

else:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    POSTGRES_DB = os.environ.get("DJANGO_DB_NAME")
    POSTGRES_USERNAME = os.environ.get("DJANGO_DB_USER")
    POSTGRES_PASSWORD = os.environ.get("DJANGO_DB_PASSWORD")
    POSTGRES_HOST = os.environ.get("DJANGO_DB_HOST")
    POSTGRES_PORT = 5432

    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': POSTGRES_DB,
                'USER': POSTGRES_USERNAME,
                'PASSWORD': POSTGRES_PASSWORD,
                'HOST': POSTGRES_HOST,
                'PORT': POSTGRES_PORT,
            }
    }




CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

OIDC_HOST = os.environ.get("OIDC_HOST", "https://accounts.einvotca.com")
OIDC_REALM = os.environ.get("OIDC_REALM", "secure")
OIDC_RP_CLIENT_ID = os.environ.get("OIDC_RP_CLIENT_ID", "backend")
OIDC_RP_CLIENT_SECRET = os.environ.get("OIDC_RP_CLIENT_SECRET", "F65h8yaarscZowrRSPq62axi8cu95Di7")

OIDC_OP_AUTHORIZATION_ENDPOINT = f'{OIDC_HOST}/realms/{OIDC_REALM}/protocol/openid-connect/auth'
OIDC_OP_TOKEN_ENDPOINT = f'{OIDC_HOST}/realms/{OIDC_REALM}/protocol/openid-connect/token'
OIDC_OP_USER_ENDPOINT = f'{OIDC_HOST}/realms/{OIDC_REALM}/protocol/openid-connect/userinfo'

TOKEN_EXPIRATION_TIME = os.environ.get("TOKEN_EXPIRATION_TIME", 300)  # Set token expiration time in seconds
TOKEN_VERIFY_EXPIRATION = True
TOKEN_VERIFY_SIGNATURE = True
TOKEN_EXPIRATION_LEEWAY = os.environ.get("TOKEN_EXPIRATION_LEEWAY", 60)

OIDC_OP_JWKS_ENDPOINT = 'https://accounts.einvotca.com/realms/secure/protocol/openid-connect/certs'
OIDC_RP_SIGN_ALGO = os.environ.get("OIDC_RP_SIGN_ALGO", 'RS256')
OIDC_RP_IDP_SIGN_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqLVXlFjR73/
3sm2wznMa6zxv/UzQ0PoaF3hChB/Ugkzel8g46IKLjSJUp780ZK2OKI
TkgmUxgddz/tfn3tlhre2F40+ZuEeE6Rnd3/pN3n2GJzrX4DmSp4Gb8
DLhBPVhVSwfEh3WtHTEGHYYyhgFYF2qRLX4OeVfyhTGHf9jBMjE7
OhgluxAn3wKn0pvs/I07xEG17roM9KMeJ4Tv7ZC5g2m5s5R1xGfmPcS
zvhCPj0q39mCp0bWlpX6kaENfxC/YuUihPsGkYdGMGt+B/cHrGAY85
bJoJrI3zNDOp8JLuC/w3qR6sZkyr8ewIoJ6pgjwHys18TweFDcy2DYE4
ybXQIDAQAB
-----END PUBLIC KEY-----"""


OIDC_CALLBACK_REDIRECT_URI = 'http://localhost:8000/api/callback/'
OIDC_RP_SCOPES = 'roles email'
OIDC_VERIFY_SSL = False
OIDC_CREATE_USER = True
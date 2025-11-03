AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
INSTALLED_APPS = [
    'accounts',
    'shop',
    ...
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

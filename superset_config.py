import os

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
SQLALCHEMY_DATABASE_URI = os.getenv('SUPERSET_META_DB_URI', 'sqlite:////var/lib/superset/superset.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY','thisISaSECRET_1234')


from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH

basedir = os.path.abspath(os.path.dirname(__file__))

superset_oauth_key = os.getenv('SUPERSET_OAUTH_KEY')
superset_oauth_secret = os.getenv('SUPERSET_OAUTH_SECRET')
superset_oauth_whitelist = os.getenv('SUPERSET_OAUTH_WHITELIST')

ROW_LIMIT = 5000
SUPERSET_WORKERS = 4

# SECRET_KEY = 'a long and random secret key'

CSRF_ENABLED = False

AUTH_TYPE = AUTH_OAUTH

AUTH_USER_REGISTRATION = True

# NOTICE:
AUTH_USER_REGISTRATION_ROLE = 'Admin'
# OAUTH_PROVIDERS = [
#     {
#         'name': 'github',
#         'icon': 'fa-github',
#         'token_key': 'access_token',
#         'whitelist' : '@houzz.com',
#         'remote_app': {
#             'base_url':'https://api.github.com/',
#             'request_token_url': None,
#             'access_token_url': 'https://github.com/login/oauth/access_token',
#             'authorize_url': 'https://github.com/login/oauth/authorize',
#             'access_token_method': 'POST',
#             'access_token_params' : {
#                 'client_id' : superset_oauth_key 
#             },
#             'request_token_params': {
#                 'scope': 'read:user,user:email'
#              },
#             'consumer_key': superset_oauth_key,
#             'consumer_secret': superset_oauth_secret
#         }
#     }
# ]

OAUTH_PROVIDERS = [
    {
        'name': 'github',
        'icon': 'fa-github',
        'token_key': 'access_token',
        'remote_app': {
            'consumer_key': superset_oauth_key,
             'consumer_secret': superset_oauth_secret,
            'base_url':'https://api.github.com/',
            'request_token_url': None,
            'access_token_url': 'https://github.com/login/oauth/access_token',
            'authorize_url': 'https://github.com/login/oauth/authorize',
            'access_token_method': 'POST',
            'request_token_params': {
                'scope': 'read:user,user:email'
             }
        }
    }
]
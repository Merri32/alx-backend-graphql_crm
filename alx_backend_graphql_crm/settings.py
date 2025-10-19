INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'crm',  # the main app
    'graphene_django',  # required for GraphQL
]
GRAPHENE = {
    'SCHEMA': 'alx_backend_graphql_crm.schema.schema',  # points to your schema.py file
}

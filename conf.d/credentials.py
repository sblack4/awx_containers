
import os 


DATABASE_USER = os.getenv('DATABASE_USER', 'awx')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'awx')
DATABASE_HOST = os.getenv('DATABASE_HOST', None)
DATABASE_PORT = int(os.getenv('DATABASE_PORT', 5432))
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'awxpassword')

MEMCACHED_HOST = os.getenv('MEMCACHED_HOST', 'memcached')
MEMCACHED_PORT = int(os.getenv('MEMCACHED_POST', '11211'))

RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'awxpass')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
RABBITMQ_VHOST = os.getenv('RABBITMQ_VHOST', 'awx')

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(
    RABBITMQ_USER, 
    RABBITMQ_PASSWORD, 
    RABBITMQ_HOST, 
    RABBITMQ_PORT,
    RABBITMQ_VHOST)
    

CHANNEL_LAYERS = {
    'default': {'BACKEND': 'asgi_amqp.AMQPChannelLayer',
                'ROUTING': 'awx.main.routing.channel_routing',
                'CONFIG': {'url': BROKER_URL}}
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '{}:{}'.format(MEMCACHED_HOST, MEMCACHED_PORT)
    },
    'ephemeral': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

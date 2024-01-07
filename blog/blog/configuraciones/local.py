from .settings import *

DATABASES = {
    "default":{
        "ENGINE": "django.db.backends.mysql",
        "NAME": "blogdb",
        "USER": "root",
        "PASSWORD": "1877",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
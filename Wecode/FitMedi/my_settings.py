SECRET = {
    "key": "8u*t9%4qqq@*7a4dxqi4jw-_xj)=b#&fp-@6&$ne)xi_%53lt#",
    "algorithm": "HS256",
}

DATABASE = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "fitmedi",
        "USER": "root",
        "PASSWORD": "dptmzbdpf",
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {"charset": "utf8mb4"},
        "TEST": {"MIRROR": "default"},
    }
}

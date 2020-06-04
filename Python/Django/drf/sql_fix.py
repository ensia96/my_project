import os, django, sys

os.chdir('Converse_REST')

sys.path.append(os.getcwd())

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "Converse_REST.settings"
)

django.setup()

from product.models import Media

for i in Media.objects.filter(media_url__contains = 'primary.jpg'):
    a = i.media_url.replace ('primary.jpg','hover.jpg')
    b = i.product_id
    Media.objects.create(
        media_url = a,
        product_id =b
    )

#from user.models import User
#
#User.objects.create(google_id = 'mango')
#
#User.objects.create(google_id = 'mango')

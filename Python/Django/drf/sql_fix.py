import os, django, sys

os.chdir('Converse_REST')

sys.path.append(os.getcwd())

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "Converse_REST.settings"
)

django.setup()

from product.models import Series

for i in Series.objects.filter(code__contains = '#'):#.values('code'):
    i.code = i.code.replace ('#','')
    i.save()
#    Media.objects.create(
#        media_url = a,
#        product_id =b
#    )

#from user.models import User
#
#User.objects.create(google_id = 'mango')
#
#User.objects.create(google_id = 'mango')

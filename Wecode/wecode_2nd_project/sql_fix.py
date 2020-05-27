import os, django, sys

os.chdir('youtubemuzic_test')

sys.path.append(os.getcwd())

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "youtubemuzic_test.settings"
)

django.setup()

from music.models import Thumbnail

for i in Thumbnail.objects.filter(url__contains = 'sddefault.jpg'):
    i.url = i.url.replace ('sddefault.jpg','maxresdefault.jpg')
    i.save()

from user.models import User

User.objects.create(google_id = 'mango')

User.objects.create(google_id = 'mango')

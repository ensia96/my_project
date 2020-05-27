import csv, os, django, sys, pymysql

#https://lh3.googleusercontent.com/fQUui0KZnT8FymPMhwcfxi55BOB3BaPKSv8k0XbgSpu_Zf5G_45T9SF-I6g0lNgJH3r2hMsG=w2880-h1613-l90-rj
#os.chdir('..')
#os.getcwd()

target = 'youtubemuzic_test'

os.chdir('youtubemuzic_test')

# delete db
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='dptmzbdpf',
    db=target,
    charset='utf8mb4'
)
curs = conn.cursor()

curs.execute('drop database '+target)
curs.execute('create database '+target+' character set UTF8mb4 collate utf8mb4_bin')

conn.close()

# delete migrations
os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
os.system('find . -path "*/migrations/*.pyc"  -delete')

# migrate
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

# append envpath
sys.path.append(
    os.getcwd()
)
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "youtubemuzic_test.settings"
)

# start django
django.setup()

from music.models import *

os.chdir('../ym_data')

# 핫리스트 ( 단순 데이터 ) 삽입

with open('./hotlist.csv', newline='') as data:

    for row in csv.DictReader(data):

        Hotlist.objects.create(
            title = row['title'],
            artist = row['artist'],
            views = row['views'],
            thumbnail = Thumbnail.objects.create(
                url = row['thumbnail']
            )
        )

# 타입 데이터 생성

for tp in ['공용','사용자','날씨','시간','싱글','EP','앨범','재생목록','차트']:
    Type.objects.create(
        name = tp
    )

os.chdir('collections')

# 핵심 데이터 삽입

# 메인 썸네일 수집 못해서 단일 데이터로 처리

basic_url = 'https://lh3.googleusercontent.com/fQUui0KZnT8FymPMhwcfxi55BOB3BaPKSv8k0XbgSpu_Zf5G_45T9SF-I6g0lNgJH3r2hMsG=w2880-h1613-l90-rj'

thumbnail, dumm = Thumbnail.objects.get_or_create(
    url   = basic_url
)

for collection in [
    element
    for element in os.listdir()
    if element != '.DS_Store'
]:

    os.chdir(collection)

    # 컬렉션 개체 생성

    if collection in ['비 내리는 날☔️','구름 많은 날☁️']:
        coll_type = Type.objects.get(
            name = '날씨'
        )
    elif collection in ['새로운 하루를 위한 준비','나를 위한 혼술시간','꿈나라로 가야할 시간']:
        coll_type = Type.objects.get(
            name = '시간'
        )
    elif collection in ['인기 차트','내 관련 재생목록']:
        coll_type = Type.objects.get(
            name = '사용자'
        )
    else:
        coll_type = Type.objects.get(
            name = '공용'
        )

    collection = Collection.objects.create(
        name      = collection,
        thumbnail = thumbnail,
        type      = coll_type
    )

    playlists = []

    # 플레이리스트 개체 생성

    with open(
        f'./playlists.csv',
        newline=''
    ) as data:

        for row in csv.DictReader(data):

            Playlist.objects.get_or_create(
                name        = row['title'],
                description = row['description'],
                year        = row['year'],
                artist      = row['artist'],
                thumbnail   = Thumbnail.objects.create(
                    url     = row['thumbnail']
                ),
                type        = Type.objects.filter(
                    name = row['type']
                ).first(),
                collection  = collection
            )
            playlists.append(row['title'])

    for playlist in [
        element
        for element in os.listdir()
        if element != '.DS_Store'
    ]:

        # 미디어 개체 생성

        if playlist != 'playlists.csv':
            with open(f'./{playlist}',newline='') as data:
                for row in csv.DictReader(data):
                    Media.objects.create(**{(
                        'name' if key == 'title'
                        else key
                    ):(Thumbnail.objects.create(url = row['thumbnail']) if key == 'thumbnail'
                       else Artist.objects.create(name = row[key]) if key == 'artist'
                       else Playlist.objects.filter(
                           name = playlists[int(playlist[:-4])]).last() if key == 'playlist'
                       else collection if key == 'collection'
                       else row[key])
                            for key in [
                                'title',
                                'thumbnail',
                                'artist',
                                'album',
                                'length',
                                'collection',
                                'playlist']})

    os.chdir('..')


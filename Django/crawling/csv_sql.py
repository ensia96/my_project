import csv, os

#https://lh3.googleusercontent.com/fQUui0KZnT8FymPMhwcfxi55BOB3BaPKSv8k0XbgSpu_Zf5G_45T9SF-I6g0lNgJH3r2hMsG=w2880-h1613-l90-rj


os.chdir('./ym_data')

collection_list = []

for i in os.listdir():
    if '2020' in i:
        with open(i, newline='') as data:
            data_reader = csv.DictReader(data)
            collection_list = list(set([row['collection'] for row in data_reader]))

newcsv = open("./collection.csv", 'w+', encoding='utf-8')

csv.writer(
    newcsv
).writerow(
    [
        'collection'
    ]
)

for collection in collection_list:

    csv.writer(
        newcsv
    ).writerow(
        [
            collection
        ])

################# for collection #################
#os.chdir('..')
################# for input data #################

#import django, sys
#
#sys.path.append(
#    os.getcwd()
#)
#os.environ.setdefault(
#    "DJANGO_SETTINGS_MODULE",
#    "converse_test.settings"
#)
#
#django.setup()
#
#from music.models import *



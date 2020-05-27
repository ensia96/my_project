import csv, os, django, sys
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "converse.settings")
django.setup()
from product.models import *
from foundation.models import *

target = './data/product.csv' # 제품과 여러 부속정보
cat     = 'category' # 카테고리
cat_gro = 'category_group' # 카테고리_그룹
cat_pro = 'product_category' # 카테고리_제품
gro = 'group' # 그룹
gro_pro = 'product_group' # 그룹_제품
col     = 'color' # 색상 일단 따로
col_pro = 'product_color' # 색상_제품
sil     = 'silhouette' # 실루엣
sil_pro = 'product_silhouette' # 실루엣_제품
siz     = 'size' # 사이즈
siz_pro = 'product_size' # 사이즈_제품

with open(f'./data/{cat}.csv', newline='') as data: # 카테고리
        data_reader = csv.DictReader(data)
        for row in data_reader:
            Category.objects.create(
                name = row[cat]
            )

with open(f'./data/{cat_gro}.csv', newline='') as data: # 그룹 (+카테고리_그룹)
    data_reader = csv.DictReader(data)
    for row in data_reader:
            Group.objects.create(
                name = row['group'],
                category = Category.objects.get(name = row[cat])
            )

with open(target, newline='') as opened: # 제품, 상품정보, 시리즈, 미디어
    data_reader = csv.DictReader(opened)
    for row in data_reader:
        if row['size_img']:
            detail_id = Detail.objects.create(
               summary     = row['summary'],
               size_img    =  row['size_img'],
               desc_img    = row['image_big'],
               information = row['information']
            )
        else:
            detail_id = Detail.objects.create(
               summary     = row['summary'],
               desc_img    = row['image_big'],
               information = row['information']
            )
        product_id = Product.objects.create(
            code   = row['code'],
            name   = row['name'],
            price  = row['price'],
            gender = row['gender'],
            color_name = row['color_name'],
            detail = detail_id
        )

        detail_strings = row['info_long']
        detail_strings = detail_strings.strip('[]')
        detail_strings = detail_strings.replace("'", "")
        detail_strings = detail_strings.replace('"','')
        detail_strings = detail_strings.replace('\n','')
        detail_strings = detail_strings.split('*')

        for i in range(len(detail_strings)):
            if i >= 1:
                strings = f"* {detail_strings[i]}".strip("''")
            else :
                strings = detail_strings[i].strip("''")
            strings.strip('"')
            descriptions = Description.objects.create(
                string   = strings.strip(','),
                product  = product_id,
            )

        series_url      = row['series_img_list']
        series_url      = series_url.strip('[]')
        series_url      = series_url.replace('"','')
        list_series_url = series_url.split(',')

        series_codes     = row['series_list']
        series_codes     = series_codes.strip('[]')
        series_codes     = series_codes.replace('"','')
        list_series_code = series_codes.split(',')

        for i in range(len(list_series_url)):
            series = Series.objects.create(
                code = list_series_code[i].strip("''"),
                image = list_series_url[i].strip("''"),
                product = product_id
            )
        media_url      = row['media_list']
        media_url      = media_url.strip('[]')
        media_url      = media_url.replace('"', '')
        list_media_url = media_url.split(',')

        for i in range(len(list_media_url)):
            Media.objects.create(
                media_url  = list_media_url[i].strip("''"),
                product = product_id
            )

with open(f'./data/{sil}.csv', newline='') as data: # 실루엣
        data_reader = csv.DictReader(data)
        for row in data_reader:
            Silhouette.objects.create(
                name = row[f'{sil}_code']
            )

with open(f'./data/{siz}.csv', newline='') as data: # 사이즈
        data_reader = csv.DictReader(data)
        for row in data_reader:
            Size.objects.create(
                size = row[siz]
            )

with open(f'./data/converse_{col}_codes.csv', newline='') as data: # 색상
        data_reader = csv.DictReader(data)
        for row in data_reader:
            Color.objects.create(
                color_code = row['color_code'],
                color_name = row['color_name']
            )

with open(f'./data/{siz_pro}.csv', newline='') as data: # 제품_사이즈
        data_reader = csv.DictReader(data)
        for row in data_reader:
            if Size.objects.filter(id=row['size_id']).exists():
                ProductSize.objects.create(
                    product = Product.objects.get(code=row['product_code']),
                    size    = Size.objects.get(id=row['size_id'])
                )

with open(f'./data/{col_pro}.csv', newline='') as data: # 제품_색상
        data_reader = csv.DictReader(data)
        for row in data_reader:
            ProductColor.objects.create(
                product = Product.objects.get(code=row['product_codes']),
                color   = Color.objects.get(id = row['color_code'])
            )

with open('./data/product_category.csv', newline='') as data: # 제품테이블에 카테고리_id 추가
    data_reader = csv.DictReader(data)
    for row in data_reader:
        foreign = Product.objects.get(code=row['product_id'])
        foreign.category = Category.objects.get(id=row['category_id'])
        foreign.save()

with open('./data/product_group.csv', newline='') as data: # 제품테이블에 그룹_id 추가
    data_reader = csv.DictReader(data)
    for row in data_reader:
        try:
            foreign = Product.objects.get(code=row['product_id'])
            foreign.group = Group.objects.get(id=row['group_id'])
            foreign.save()
        except Exception:
            pass

with open('./data/product_silhouette.csv', newline='') as data: # 제품테이블에 실루엣_id 추가
    data_reader = csv.DictReader(data)
    for row in data_reader:
        foreign = Product.objects.get(code=row['product_codes'])
        foreign.silhouette = Silhouette.objects.get(name=row['silhouette'])
        foreign.save()

sneakers_list = ['560251C','167324C', '167966C', '167963C', '164057C', '164056C', '162054C', '162063C', '566751C', '567157C', '567311C', '567155C', '567309C', '166810C', '167291C', '167292C', '162350C', '162351C', '163343C', '167322C', '167323C', '567992C', '567991C', '567101C', '567100C', '566766C', '166838C', '166839C', '166713C', '166712C', '167058C', '166809C', '167071C', '167061C', '167072C', '166861C', '167970C', '167971C', '167347C', '567143C', '167345C', '167346C', '167067C', '167068C', '167069C', '166813C', '166812C', '167237C', '166854C', '166853C', '166855C', '166725C', '166726C', '167043C', '167044C', '166749C', '166747C', '567105C', '166745C', '166744C', '166740C', '166741C', '166703C', '166702C', '167106C', 'M9166C', '167326C', '167967C', '166851C', '166849C', '166850C', '166825C', '166824C', '166827C', '166826C', '167329C', '167327C', '167051C', '166803C', 'M9696C', '165742C', '165741C', '565062C', '164225C', '164224C', '164952C', '164947C', '164950C', '164945C', '164951C', '164946C', '164949C', '164944C', '161577C', '158369C', '162065C', '162056C', '162062C', '162053C', '162058C', '162050C', 'M5039C', 'M9697C', 'M7652C', 'M3310C', 'M9622C', 'M9621C', 'M7650C', 'M9160C']


for sneakers_code in sneakers_list:
    product = Product.objects.get(code = sneakers_code)
    product.is_sneakers = True
    product.save()

with open('./data/converse_instagram.csv', newline='') as data:
    data_reader = csv.DictReader(data)
    for row in data_reader:
        Instagram.objects.create (
            thumbnail = row['thumbnail'],
            profile_image = row['profile_img'],
            user = row['username'],
            created_at = row['created_at']
        )

is_main_page_list = ['167645C', '167642C', '10018896-A02', '10018896-A01', '167854C', '167853C', '167866C', '165907C', '166804C', '167804C', '167706C', '165024C', '167631C', '167810C', '163407C' ]

#product_id, color_id
aa = [[59,1],[70,1],[72,1],[74,1],[85,1],[88,1],[95,1],[97,1],[99,1],[101,1],[110,1],[111,1],[122,1],[130,1],[133,1],[137,1],[138,1],[145,1],[146,1],[147,1],[148,1],[153,1],[159,1],[160,1],[161,1],[164,1],[167,1],[177,1],[182,1],[183,1],[184,1],[187,1],[191,1],[250,11]]

for i in range(len(aa)):
    ProductColor.objects.create(
        product=Product.objects.filter(id=aa[i][0])[0],
        color=Color.objects.filter(id=aa[i][1])[0]
    )

for main_code in is_main_page_list:
    product = Product.objects.get(code = main_code)

    product.is_main_page = True
    product.save()

with open('./data/converse_stores.csv', newline='') as data:
    StoreType.objects.create(
        name = '단독매장'
    )
    StoreType.objects.create(
        name = '백화점/쇼핑몰'
    )
    data_reader = csv.DictReader(data)
    for row in data_reader :
        Store.objects.create(
            name = row['name'],
            address1 = row['address1'],
            address2 = row['address2'],
            city     = row['city'],
            phone    = row['phone'],
            longitude = row['longitude'],
            latitude = row['latitude'],
            state    = row['state'],
            store_type = StoreType.objects.get(name =row['storeType']),
        )

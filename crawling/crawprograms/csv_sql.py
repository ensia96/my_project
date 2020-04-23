import csv, os, django, sys

# manage.py 에 접근하기 위한 디렉토리 커서 위치 이동
os.chdir("..")
print(os.getcwd())

# self 파일 절대경로와 경로명 변수에 할당
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR=", end=""), print(BASE_DIR)
print(os.path.abspath(__file__))

# 파이썬 프로그램의 경로객체에 manage.py 파일이 있는 디렉토리로의 접근 경로를 추가
sys.path.append(BASE_DIR)

# os 의 환경변수에 장고와 DB설정을 기본값으로 설정 ( 장고프로그램 설정모듈과 현재 프로젝트의 세팅 )
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cks_sqlite.settings")
# 개별적인 장고 사용 ( manage.py 를 shell 로 동작 )
django.setup()

# ↑ 이 시점부터 python manage.py shell 로 동작한 상황과 같은 환경

# 처리할 모델에 대한 참조구문
from product.models import *

# 사용할 csv파일 지정변수 선언
CSV_PATH = './db/csv/first_1_menu.csv'

# csv 파일
with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)

	for row in data_reader:
		print(row)
		Menu.objects.create(
			name = row['\ufeffname']
		)
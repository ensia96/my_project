import os, pymysql

# MySQL 에서 사용하는 데이터베이스의 이름을 넣어주세요!
target = 'youtubemuzic_test'

# MySQL 의 사용자 값을 넣어주세요! ( root 라면 그대로 두세요! )
sqlusr = 'root'

# MySQL 의 비밀번호 값을 넣어주세요! ( 없다면, '' 을 넣어주세요!)
sqlpwd = 'dptmzbdpf'

def migrating():
    # delete db
    conn = pymysql.connect(
        host='localhost',
        user=sqlusr,
        password=sqlpwd,
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

migrating()

SECRET= 'z1!bfm&_)4m1no)rpjl4tc9sb&wsln$@y)w=s7d794lsqw4oc9'

DATABASES = {
	'default' : {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'converse',
		'USER': 'root',
		'PASSWORD': 'dptmzbdpf',
        'HOST': 'wecode-project.cyfp0gaqdrrv.ap-northeast-2.rds.amazonaws.com',
		'PORT': '3306',
		'OPTIONS': {'charset': 'utf8mb4'},
		'TEST': {
			'CHARSET': 'utf8mb4',
			'COLLATION': 'utf8mb4_general_ci'
		}
	}
}

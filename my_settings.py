SECRET_KEY={
    'secret' : '2*e!kc(g05ks30*_b=x(u((395gvk1b7z*1_jv!y*^4_b_)qld'
}

DATABASES = {
	'default' : {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'converse_test',
		'USER': 'root',
		'PASSWORD': 'dptmzbdpf',
		'HOST': 'localhost',
		'PORT': '3306',
		'OPTIONS': {'charset': 'utf8mb4'},
		'TEST': {
			'CHARSET': 'utf8mb4',
			'COLLATION': 'utf8_general_ci'
		}
	}
}
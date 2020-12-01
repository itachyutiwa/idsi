from serverpjt.settings import *
import dj_database_url

DEBUG =False
TEMPLATES_DEBUG = False
DATABASES['default'] = dj_database_url.config()
SECRET_KEY = '-n(jxc8!_n@gg!kq$nvnyp1=em2l3rg=ib)-al7($*d*ofs6om'
ALLOWED_HOSTS = ['idsi.herokuapp.com']



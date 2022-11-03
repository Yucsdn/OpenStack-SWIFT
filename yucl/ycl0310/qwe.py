import os
from django.utils.encoding import escape_uri_path
file = '请按照.txt'
os.system('del "D:\swift\download\{}" /F'.format(escape_uri_path(file)))
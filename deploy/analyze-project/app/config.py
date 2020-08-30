# this is a sample config file. rename it to `config.py` and edit accordingly

API_KEY = 'put your API key from kavenegar here'

# Mysql configs
MYSQL_HOST = 'db'
MYSQL_PORT= 3306
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'Azahmadi@4466'
MYSQL_DB_NAME = 'flask'

# call back url from KaveNegar will look like
# /v1/CALL_BACK_TOKEN/process
CALL_BACK_TOKEN = 'CALL BACK TOKEN'

# login cedentials
USERNAME = 'parham'
PASSWORD = '123'

# generate one strong secret key for flask.
SECRET_KEY = 'random long string with alphanumeric + #()*&'


### Do not change below unless you know what you are doing
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = {'xlsx'} 

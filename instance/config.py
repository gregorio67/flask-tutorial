import os

# grab the folder of the top-level directory of this project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

# Update later by using a random number generator and moving
# the actual key outside of the source code under version control
#SECRET_KEY = '<INSERT FROM RANDOM STRING GENERATED>'
DEBUG = True

#SERVER_NAME='192.168.11.93:9000'

SECRET_KEY = 'dev'
DATABASE = os.path.join(BASE_DIR, 'flaskr.sqlite')

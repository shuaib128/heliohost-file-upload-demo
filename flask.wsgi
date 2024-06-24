import os
import sys

# Edit your path below
sys.path.append("/home/shuiab/httpdocs/flaskapp")

sys.path.insert(0, os.path.dirname(__file__))
from app import app as application

# Set this to something harder to guess
application.secret_key = 'your_secret_key'

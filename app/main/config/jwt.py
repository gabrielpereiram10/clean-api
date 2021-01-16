import os
import jwt

key = os.environ.get('JWT_SECRET_KEY')
algorithm = os.environ.get('algorithm')

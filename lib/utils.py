__author__ = 'bluzky'
import re
import random
import string
from datetime import datetime
from flask import current_app
from itsdangerous import URLSafeSerializer

_EMAIL_REGEX = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'  # quoted-string
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE  # domain
    )

_URL_REGEX = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def is_email_address_valid(address):
    is_valid = _EMAIL_REGEX.match(address)
    return is_valid

def is_valid_url(url):
    return _URL_REGEX.match(url)

def generate_id(size=12, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def is_id_valid(id):
    try:
        id = int(id)
        return True if id > 0 else False
    except:
        return False

def get_slug_from_string(string):

    result = ""
    for char in string:
        if not char.isalpha() and not char.isdigit():
            result += " "
        else:
            result += char
    result = result.strip().lower()
    result = result.replace(" ", "-")
    return result

READMORE_TAG = "<!--more-->"
def has_readmore_tag(text):
    if text.find(READMORE_TAG) > 0:
        return True
    else:
        return False

def get_to_readmore(text):
    pos = text.find(READMORE_TAG)
    if pos > 0:
        return text[:pos]
    else:
        return text


SHORT_CONTENT_LENGTH = 400
def get_short_content(text):
    if len(text) >= SHORT_CONTENT_LENGTH :
        return text[:text[:SHORT_CONTENT_LENGTH].rfind(' ')] + ' ...'
    else:
        return text + '...'


def generate_activation_token(email, code, expired_in=84600):
    """
    Create token from given email, code and valid duration
    :param email:
    :param code:
    :param expired_in: default is 24 hours
    :return:
    """
    expired_at = (datetime.utcnow() - datetime(1970,1,1)).total_seconds() + expired_in
    args = (email, code, expired_at)
    s = URLSafeSerializer(current_app.config["SECRET_KEY"])
    return s.dumps(args)

def is_activation_token_valid(token):
    s = URLSafeSerializer(current_app.config["SECRET_KEY"])
    try:
        info = s.loads(token)
        expired_at = info[2]
        if expired_at < (datetime.now() - datetime(1970,1,1)).total_seconds():
            return False
        else:
            return True
    except:
        return False

def extract_activation_info(token):
    s = URLSafeSerializer(current_app.config["SECRET_KEY"])
    try:
        return s.loads(token)
    except:
        return None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']

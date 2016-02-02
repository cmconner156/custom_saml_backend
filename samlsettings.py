import logging

logging.warn("Using custom samlsettings")

from desktop.settings import *
from libsaml.saml_settings import *

SAML_AUTHENTICATION = True
LOGIN_URL = '/saml2/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


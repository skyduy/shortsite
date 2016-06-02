# coding: utf-8

# import os
# import sys
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'site_packages'))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/shortsite/")


from Urlshorter.app import create_app
application = create_app()


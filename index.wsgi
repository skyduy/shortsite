#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/shortsite/")

from Urlshorter.app import create_app
application = create_app()

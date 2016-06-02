#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/path/to/folder/shortsite/")

from Urlshorter.app import create_app
application = create_app()

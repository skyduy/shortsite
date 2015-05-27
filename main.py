# coding: utf-8

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'site_packages'))

from Urlshorter.app import create_app
app = create_app(debug=True)

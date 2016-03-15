#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Special live-site-only variables
SITEURL = 'https://www.andrewheiss.com'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

FEED_ALL_ATOM = 'atom.xml'

GOOGLE_ANALYTICS = 'UA-527449-5'

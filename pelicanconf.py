#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site development flag
developing_site = True

#-------------------
# Site information
#-------------------
AUTHOR = 'Andrew Heiss'
SITENAME = 'Andrew Heiss'
MINIBIO = 'Scholar, developer, and designer'

SITEURL = ''

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%A, %B %-d, %Y'


#----------------
# Site building
#----------------
# Theme
THEME = '/Users/andrew/Development/•Pelican/themes/athpelican-theme'

# Folder where everything lives
PATH = 'content'

# Pagination
# DEFAULT_PAGINATION = 10

# Plugins
PLUGIN_PATHS = ['/Users/andrew/Development/•Pelican/pelican-plugins']
PLUGINS = ['pandoc_reader']

# Special pandoc settings
PANDOC_ARGS = [
    '--smart',
    '--base-header-level=2'
]

# Nice typographic things
TYPOGRIFY = True

# Structure of output folder
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Include source files, just for fun
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.txt'

# Feed generation
FEED_ALL_ATOM = None if developing_site else None
CATEGORY_FEED_ATOM = None if developing_site else None
TRANSLATION_FEED_ATOM = None if developing_site else None
AUTHOR_FEED_ATOM = None if developing_site else None
AUTHOR_FEED_RSS = None if developing_site else None

# Cache
LOAD_CONTENT_CACHE = False if developing_site else True


#-------------
# Site items
#-------------
MENUITEMS = [('About', '#'), ('CV', '#'), ('Research', '#'),
             ('Teaching', '#'), ('Blog', '#'), ('Portfolio', '#')]

SOCIAL = [('E-mail', 'mailto:andrew@andrewheiss.com', 'fa-envelope-square'),
          ('Heissatopia (family blog)', 'http://www.heissatopia.com', 'fa-smile-o'),
          ('Facebook', 'https://www.facebook.com/andrewheiss', 'fa-facebook-square'),
          ('Twitter', 'https://twitter.com/andrewheiss', 'fa-twitter-square'),
          ('GitHub', 'https://github.com/andrewheiss', 'fa-github-square'),
          ('StackOverflow', 'https://stackoverflow.com/users/120898/andrew', 'fa-stack-overflow'),
          ('LinkedIn', 'https://www.linkedin.com/in/andrewheiss', 'fa-linkedin-square'),
          ('Google+', 'https://plus.google.com/+AndrewHeiss', 'fa-google-plus-square'),
          ('Academia.edu', 'https://duke.academia.edu/AndrewHeiss', 'fa-graduation-cap')]

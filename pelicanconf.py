#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

addons = os.environ['HOME']+'/Projects/pelican-addons/'

AUTHOR = 'robotics-grimoire'
SITENAME = 'The Robotics Grimoire'
SITEURL = ''

# Show us the way
PATH = 'content'
ARTICLE_PATH = 'articles'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images']

# Internationalization
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
MARKUP = ('md', 'ipynb')
IPYNB_USE_METACELL = True

PLUGIN_PATHS = [addons + 'pelican-plugins']
PLUGINS = [
    'better_codeblock_line_numbering',
    'render_math',
    'related_posts',
    'ipynb.markup',
]

# Themes
# THEME = 'attila'
HOME_COVER = 'images/Tron.jpg'
AUTHORS_BIO = {
  'John': {
    'name': 'John Hill',
    'image': 'images/Light.jpg',
    'linkedin': 'https://www.linkedin.com/in/jhill515',
    'stackoverflow': 'https://stackoverflow.com/users/story/2370362',
    'location': 'Pittsburgh',
    'bio': 'Keep on creating!',
  }
}


# Fixed menu items
MENUITEMS = (
    ('Blog', 'https://robotics-grimoire.github.io'),
    ('About', '/pages/about.html'),
    ('References', '/pages/references.html'),
)

# Dynamic menu items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('GitHub', 'http://github.com/'),
)

# Social widgets
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/jhill515'),
    ('Stack Overflow', 'https://stackoverflow.com/users/story/2370362'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

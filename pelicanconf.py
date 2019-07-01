#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

addons = os.environ['HOME']+'/Projects/pelican-addons/'

AUTHOR = 'robotics-grimoire'
SITENAME = 'The Robotics Grimoire'
SITEURL = ''
DISQUS_SITENAME = 'robotics-grimoire.disqus.com'

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

### THEME SETUP ###
THEME = addons + 'pelican-themes/pelican-clean-blog' # See https://github.com/molivier/nest
HEADER_COVER = 'images/Tron.jpg'
HEADER_COLOR = 'white'
COLOR_SCHEME_CSS = 'darkly.css'

# Custom Footer
FOOTER_INCLUDE = 'customfooter.html'
IGNORE_FILES = [FOOTER_INCLUDE]
EXTRA_TEMPLATES_PATHS = [os.path.dirname(__file__)]

# Fixed menu items
MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Archive', '/archives.html'),
    ('Tags', '/tags.html'),
    ('Links', '/pages/links.html'),
    ('Reference', '/pages/references.html'),
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
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/jhill515'),
    ('Stack Overflow', 'https://stackoverflow.com/users/story/2370362'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

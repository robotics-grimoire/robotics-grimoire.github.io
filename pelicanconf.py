#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

addons = os.environ['HOME']+'/Projects/pelican-addons/'

AUTHOR = 'John Hill'
SITENAME = 'The Robotics Grimoire'
SITEURL = 'https://robotics-grimoire.github.io'
# DISQUSURL = 'https://robotics-grimoire.github.io'
DISQUS_SITENAME = 'robotics-grimoire'

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
    'pelican_gist',
]

### THEME SETUP ###
THEME = addons + 'pelican-themes/pelican-clean-blog' # See https://github.com/gilsondev/pelican-clean-blog
HEADER_COVER = 'images/Tron.jpg'
HEADER_COLOR = 'white'
COLOR_SCHEME_CSS = 'darkly.css'

# Fixed menu items
MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Archive', '/archives.html'),
    ('Tags', '/tags.html'),
    ('Links', '/pages/links.html'),
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
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/jhill515'),
    ('Stack Overflow', 'https://stackoverflow.com/users/story/2370362'),
)

DEFAULT_PAGINATION = 10

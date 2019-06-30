#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'robotics-grimoire'
SITENAME = 'The Robotics Grimoire'
SITEURL = ''

PATH = 'content'
ARTICLE_PATH = 'articles'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Blog', 'https://robotics-grimoire.github.io'),
    ('About', '/pages/about.html'),
    ('References', '/pages/references.html'),
    )

PLUGIN_PATHS = [os.environ['HOME']+'/Projects/pelican-plugins']
PLUGINS = [
    'better_codeblock_line_numbering',
    'render_math',
    'related_posts',
    ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('GitHub', 'http://github.com/'),
    )

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/jhill515'),
    ('Stack Overflow', 'https://stackoverflow.com/users/story/2370362'),
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# coding=utf-8

from __future__ import unicode_literals
import os

LOCALE = 'en_US'
MARKDOWN = {}
AUTHOR = u'Sebastiaan Math\xf4t'
SITENAME = u'Dutch Society for Brain and Cognition'
STATIC_PATHS = ['pages']
ROOT_PATH = os.getcwd()
OUTPUT_PATH = 'output/'
PATH = 'content'
THEME = 'themes/cogsci'
TIMEZONE = 'Europe/Paris'
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'
DEFAULT_LANG = u'en'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 250

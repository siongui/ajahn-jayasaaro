#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ajahn Jayasāro'
SITENAME = u'Ajahn Jayasāro'
# leave SITEURL blank when developing
SITEURL = ''

PATH = 'content'

# avoid processing .html files
READERS = {'html': None}

# mix articles and static files in the same place
# @see https://github.com/getpelican/pelican/issues/1587
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['articles', 'extra', 'code']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/yezi.png': {'path': 'favicon.ico'},}

# modify TIMEZONE to your timezone
TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'
LOCALE = 'en_US.UTF-8'

# @see http://docs.getpelican.com/en/latest/settings.html#basic-settings
# @see http://docs.getpelican.com/en/latest/settings.html#path-metadata
#PATH_METADATA = 'articles/(?P<date>\d{4}/\d{2}/\d{2})/(?P<slug>[-a-zA-Z0-9.]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'
PATH_METADATA = 'articles/(?P<slug>[-a-zA-Z0-9.]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'

# @see http://docs.getpelican.com/en/latest/settings.html#url-settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# other possible PATH and URL config
#PATH_METADATA = 'articles[-a-zA-Z0-9/]*/(?P<slug>[-a-zA-Z0-9]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'
#PATH_METADATA = 'articles/(?P<urlpath>[-a-zA-Z0-9/]*)/(?P<slug>[-a-zA-Z0-9]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'
#ARTICLE_URL = '{urlpath}/{slug}/'
#ARTICLE_SAVE_AS = '{urlpath}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# https://github.com/getpelican/pelican/issues/1513
# {tag}tagName syntax not working now
# Update: 3.6.3 looks working now

THEME = 'theme'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites',
           'edit_on_github',
           'adsense',
           'embed_github_repository_file',
           'embed_picasaweb_image']

# custom setting for HTML meta info
META_KEYWORDS = 'Ajahn Jayasāro'
META_DESCRIPTION = 'Ajahn Jayasāro'

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
  'th': {
    'SITENAME': 'พระอาจารย์ชยสาโร',
    'AUTHOR': 'พระอาจารย์ชยสาโร',
    'DEFAULT_LANG': 'Thai',
    'LOCALE': 'th_TH.UTF-8',
    'META_KEYWORDS': 'พระอาจารย์ชยสาโร',
    'META_DESCRIPTION': 'พระอาจารย์ชยสาโร',
  },
}
I18N_UNTRANSLATED_ARTICLES = 'remove'

# generate only index.html and pages and articles. (no archives, tags, categories)
#DIRECT_TEMPLATES = ['index']
# use metadata attribute 'order' in page files for ordering
# @see http://docs.getpelican.com/en/latest/settings.html#url-settings
PAGE_ORDER_BY = 'order'

# CONTENT_DIR_URL is the setting for edit_on_github plugin
CONTENT_DIR_URL = u'https://github.com/siongui/ajahn-jayasaaro/tree/master/content'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# custom Jinja2 filter
def hidden_pages_get_page_with_slug_index(hidden_pages):
    for page in hidden_pages:
        if page.slug == "index":
            return page

# custom Jinja2 filter for localizing theme
def gettext(string, lang):
    if lang == "en":
        return string
    elif lang == "zh":
        if string == "Archives": return "歸檔"
        elif string == "Categories": return "分類"
        elif string == "Category": return "分類"
        elif string == "Authors": return "作者"
        elif string == "Author": return "作者"
        elif string == "Tags": return "標籤"
        elif string == "Updated": return "更新"
        elif string == "Translation(s)": return "翻譯"
        elif string == "Edit on Github": return "在Github上編輯"
        else: return string
    elif lang == "th":
        if string == "Archives": return "สารบรรณ"
        elif string == "Categories": return "ประเภท"
        elif string == "Category": return "ประเภท"
        elif string == "Authors": return "ผู้เขียน"
        elif string == "Author": return "ผู้เขียน"
        elif string == "Tags": return "แท็ก"
        elif string == "Updated": return "การปรับปรุง"
        elif string == "Translation(s)": return "การแปล"
        elif string == "Edit on Github": return "แก้ไขที่ Github"
        else: return string
    else:
        return string

JINJA_FILTERS = {
    "hidden_pages_get_page_with_slug_index": hidden_pages_get_page_with_slug_index,
    "gettext": gettext,
}

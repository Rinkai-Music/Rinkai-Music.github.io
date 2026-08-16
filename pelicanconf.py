AUTHOR = 'RINKAI'
SITENAME = "RINKAI's Homepage"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

##########
FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/' + FAVICON: {'path': FAVICON},
}
##########

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Link
LINKS = [
    ("YouTube", "https://youtube.com/channel/UCNm0hb-n5Apt6GWajJ6S8Og/?sub_confirmation=1"),
    ("Twitter", "https://x.com/TCP_Hz"),
    ("LINK3", "https://getpelican.com/"),
    ("LINK4", "https://getpelican.com/"),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

##########
# ------------------------- #
#  Site Configuration File  #
# ------------------------- #

# Variables set here will be available in template files under a `site` attribute,
# e.g. {{ site.title }}.

# Choose the theme to use when building your site. This variable should specify
# the name of a theme directory in your site's 'lib' folder.
theme = "carbon"

# Site title.
title = "Soothsayer's blog"

# Site tagline.
tagline = "A lazy guy interested with CG/database/KV/OS."

extensions = ["holly"]

holly = {
    "homepage": {
        "root_urls": "@root/notes//",
    },
    "roots": [
        {
            "root_url": "@root/notes//",
        },
    ],
}

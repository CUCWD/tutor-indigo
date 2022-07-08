from glob import glob
import copy
import os
import pkg_resources

from tutor import hooks

from .__about__ import __version__


################# Configuration

EDUCATEWORKFORCE_BLUE = "#1f5f78"
EDUCATEWORKFORCE_GREEN = "#84C299"
EDUCATEWORKFORCE_BROWN = "#655B52"
EDUCATEWORKFORCE_GRAY = "#48555d"
EDUCATEWORKFORCE_RED = "#c44936"

# Default settings for `indigo` theme. Overrides for individual sites will follow.
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "WELCOME_MESSAGE": "The place for all your online learning",
        "PRIMARY_COLOR": "#3b85ff",  # cool blue
        # Footer links are dictionaries with a "title" and "url"
        # To remove all links, run:
        # tutor config save --set INDIGO_FOOTER_NAV_LINKS=[] --set INDIGO_FOOTER_LEGAL_LINKS=[]
        "FOOTER_NAV_LINKS": [
            {"title": "About", "url": "/about"},
            {"title": "Contact", "url": "/contact"},
        ],
        "FOOTER_LEGAL_LINKS": [
            {"title": "Terms of service", "url": "/tos"},
            {
                "title": "Indigo theme for Open edX",
                "url": "https://github.com/overhangio/tutor-indigo",
            },
        ],
    },
    "unique": {},
    "overrides": {},
}

# Configuration overrides for `caregiver`
config_caregiver = copy.deepcopy(config)
config_caregiver["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `choose-aerospace`
config_choose_aerospace = copy.deepcopy(config)
config_choose_aerospace["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `educateworkforce`
config_educateworkforce = copy.deepcopy(config)
config_educateworkforce["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `harford-community-college`
config_harford_community_college = copy.deepcopy(config)
config_harford_community_college["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `meep`
config_meep = copy.deepcopy(config)
config_meep["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `ncatech`
config_ncatech = copy.deepcopy(config)
config_ncatech["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `photonics`
config_photonics = copy.deepcopy(config)
config_photonics["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `spartanburg`
config_spartanburg = copy.deepcopy(config)
config_spartanburg["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `thin-school`
config_thin_school = copy.deepcopy(config)
config_thin_school["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE

# Configuration overrides for `trustworks-cymanii`
config_trustworks_cymanii = copy.deepcopy(config)
config_trustworks_cymanii["defaults"]["PRIMARY_COLOR"] = EDUCATEWORKFORCE_BLUE


# Theme templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutorindigo", "templates")
)
# This is where the theme is rendered in the openedx build directory
# In the `dev` environment this is 
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("caregiver", "build/openedx/themes"),
        ("choose-aerospace", "build/openedx/themes"),
        ("educateworkforce", "build/openedx/themes"),
        ("harford-community-college", "build/openedx/themes"),
        ("indigo", "build/openedx/themes"),
        ("meep", "build/openedx/themes"),
        ("ncatech", "build/openedx/themes"),
        ("photonics", "build/openedx/themes"),
        ("spartanburg", "build/openedx/themes"),
        ("thin-school", "build/openedx/themes"),
        ("trustworks-cymanii", "build/openedx/themes"),
    ],
)

# Copy the SCSS partial files over to the tutor env. It appears this partials directory is 
# ignored by default by tutor/env.py `ENV_PATTERNS_IGNORE`.
hooks.Filters.ENV_PATTERNS_INCLUDE.add_items(
    [
        # Include files from "partials" folders
        r"(.*/)?partials(/.*)?$",
    ]
)


# Load all configuration entries for `caregiver`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"CAREGIVER_{key}", value) for key, value in config_caregiver["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"CAREGIVER_{key}", value) for key, value in config_caregiver["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_caregiver["overrides"].items()))


# Load all configuration entries for `choose-aerospace`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"CHOOSE_AEROSPACE_{key}", value) for key, value in config_choose_aerospace["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"CHOOSE_AEROSPACE_{key}", value) for key, value in config_choose_aerospace["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_choose_aerospace["overrides"].items()))


# Load all configuration entries for `educateworkforce`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"EDUCATEWORKFORCE_{key}", value) for key, value in config_educateworkforce["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"EDUCATEWORKFORCE_{key}", value) for key, value in config_educateworkforce["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_educateworkforce["overrides"].items()))


# Load all configuration entries for `harford-community-college`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"HARFORD_COMMUNITY_COLLEGE_{key}", value) for key, value in config_harford_community_college["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"HARFORD_COMMUNITY_COLLEGE_{key}", value) for key, value in config_harford_community_college["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_harford_community_college["overrides"].items()))


# Load all configuration entries for `indigo`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"INDIGO_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"INDIGO_{key}", value) for key, value in config["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))


# Load all configuration entries for `meep`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"MEEP_{key}", value) for key, value in config_meep["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"MEEP_{key}", value) for key, value in config_meep["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_meep["overrides"].items()))


# Load all configuration entries for `ncatech`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"NCATECH_{key}", value) for key, value in config_ncatech["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"NCATECH_{key}", value) for key, value in config_ncatech["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_ncatech["overrides"].items()))


# Load all configuration entries for `photonics`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"PHOTONICS_{key}", value) for key, value in config_photonics["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"PHOTONICS_{key}", value) for key, value in config_photonics["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_photonics["overrides"].items()))


# Load all configuration entries for `spartanburg`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"SPARTANBURG_{key}", value) for key, value in config_spartanburg["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"SPARTANBURG_{key}", value) for key, value in config_spartanburg["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_spartanburg["overrides"].items()))


# Load all configuration entries for `thin-school`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"THIN_SCHOOL_{key}", value) for key, value in config_thin_school["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"THIN_SCHOOL_{key}", value) for key, value in config_thin_school["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_thin_school["overrides"].items()))


# Load all configuration entries for `trustworks-cymanii`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"TRUSTWORKS_CYMANII_{key}", value) for key, value in config_trustworks_cymanii["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"TRUSTWORKS_CYMANII_{key}", value) for key, value in config_trustworks_cymanii["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config_trustworks_cymanii["overrides"].items()))


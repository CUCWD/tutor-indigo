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

EDUCATEWORKFORCE_LMS_HOST_PROD_DEFAULT = "{{ LMS_HOST }}"
EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT = "{{ CMS_HOST }}"
EDUCATEWORKFORCE_SUPPORT_EMAIL = "support@educateworkforce.com"
EDUCATEWORKFORCE_DEFAULT_FROM_EMAIL = "no-reply@educateworkforce.com"

ENVIRONMENT = "development"
MKG_HOST = "localhost:8080"

# If the `tutor-educateworkforce-config` plugin has set the `BASE_DOMAIN` then we're in a staging or production environment.
# This would indicate that the site is no in development environment.
if "{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}":
    ENVIRONMENT = "production"
    MKG_HOST = "{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}"


# Default settings for `indigo` theme. Overrides for individual sites will follow.
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "PLATFORM_NAME": "EducateWorkforce",
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
        "CONTACT_EMAIL": EDUCATEWORKFORCE_SUPPORT_EMAIL,
        "DEFAULT_FROM_EMAIL": EDUCATEWORKFORCE_DEFAULT_FROM_EMAIL,
        "SUPPORT_EMAIL": EDUCATEWORKFORCE_SUPPORT_EMAIL,

        "SESSION_COOKIE_DOMAIN": "",
        "BADGR_ISSUER_SLUG": "",
        "MKG_ROOT_URL": MKG_HOST,
    },
    "unique": {},
    "overrides": {
        # "LMS_HOST": "local.overhang.io:8000",  # Need to remove these before commit. This is for dev testing.
        # "CMS_HOST": "studio.local.overhang.io:8001",  # Need to remove these before commit. This is for dev testing.
        # "PLATFORM_NAME": "EducateWorkforce",
    },
    "sites": {
        "CAREGIVER": {
            "production": {
                "LMS_HOST": "caregiver.{{ LMS_HOST }}", # "caregiver.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.caregiver.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.caregiver.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                # "BADGR_ISSUER_SLUG": "",
                # "MKG_ROOT_URL": f"caregiver.{MKG_HOST}",
            },
            "development": {
                "LMS_HOST": "caregiver.{{ LMS_HOST }}",
                "CMS_HOST": "caregiver.{{ CMS_HOST }}",
                "MFE_HOST": "apps.caregiver.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                # "BADGR_ISSUER_SLUG": "",
                "MKG_ROOT_URL": f"caregiver.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - Caregiver",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ]
            }
        },
        "CHOOSE_AEROSPACE": {
            "production": {
                "LMS_HOST": "courses.chooseaerospace.org",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.courses.chooseaerospace.org",
                "SESSION_COOKIE_DOMAIN": ".courses.chooseaerospace.org",
                "BADGR_ISSUER_SLUG": "3HNkqeHmRhe3-IEvYYNmcg",
                "MKG_ROOT_URL": f"learn.chooseaerospace.org",
            },
            "development": {
                "LMS_HOST": "chooseaerospace.{{ LMS_HOST }}",
                "CMS_HOST": "chooseaerospace.{{ CMS_HOST }}",
                "MFE_HOST": "apps.chooseaerospace.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                "BADGR_ISSUER_SLUG": "TtGR95PLToqqhLucWwN0wA",
                "MKG_ROOT_URL": f"chooseaerospace.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - Choose Aerospace, Inc.",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "EDUCATEWORKFORCE": {
            "production": {
                "LMS_HOST": EDUCATEWORKFORCE_LMS_HOST_PROD_DEFAULT, # "courses.educateowrkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                "BADGR_ISSUER_SLUG": "XPPH2eGlT0KhekfWpCAWyA",
                "MKG_ROOT_URL": f"{MKG_HOST}", # "educateworkforce.com"
            },
            "development": {
                "LMS_HOST": "educateworkforce.{{ LMS_HOST }}",
                "CMS_HOST": "educateworkforce.{{ CMS_HOST }}",
                "MFE_HOST": "apps.educateworkforce.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                "BADGR_ISSUER_SLUG": "npqlh0acRFG5pKKbnb4SRg",
                "MKG_ROOT_URL": f"educateworkforce.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }}",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "HARFORD_COMMUNITY_COLLEGE": {
            "production": {
                "LMS_HOST": "harford.{{ LMS_HOST }}", # "harford.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.harford.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.harford.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                "BADGR_ISSUER_SLUG": "44bnWQE5TiSI7opBUIqyDA",
                "MKG_ROOT_URL": f"harford.{MKG_HOST}", # "harford.educateworkforce.com"
            },
            "development": {
                "LMS_HOST": "harford.{{ LMS_HOST }}",
                "CMS_HOST": "harford.{{ CMS_HOST }}",
                "MFE_HOST": "apps.harford.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                "BADGR_ISSUER_SLUG": "qkkTvDT_TBm811TKRdJLUA",
                "MKG_ROOT_URL": f"harford.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - Harford Community College",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "MEEP": {
            "production": {
                "LMS_HOST": "meep.{{ LMS_HOST }}", # "meep.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.meep.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.meep.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                "BADGR_ISSUER_SLUG": "X_gnRW0hQ7G1ycy9e_8P2w",
                "MKG_ROOT_URL": f"meep.{MKG_HOST}", # "meep.educateworkforce.com"
            },
            "development": {
                "LMS_HOST": "meep.{{ LMS_HOST }}",
                "CMS_HOST": "meep.{{ CMS_HOST }}",
                "MFE_HOST": "apps.meep.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                "BADGR_ISSUER_SLUG": "ExCOJ43VT1-koZwK8zYpIw",
                "MKG_ROOT_URL": f"meep.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - MEEP",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "NCATECH": {
            "production": {
                "LMS_HOST": "ncatech.{{ LMS_HOST }}", # "ncatech.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.ncatech.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.ncatech.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                "BADGR_ISSUER_SLUG": "3EoLJ3pmR9KFCPVG9eLWZA",
                "MKG_ROOT_URL": f"ncatech.{MKG_HOST}", # "ncatech.educateworkforce.com"
            },
            "development": {
                "LMS_HOST": "ncatech.{{ LMS_HOST }}",
                "CMS_HOST": "ncatech.{{ CMS_HOST }}",
                "MFE_HOST": "apps.ncatech.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                "BADGR_ISSUER_SLUG": "NoEnAQlVSyOQXU-Um5B37g",
                "MKG_ROOT_URL": f"ncatech.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - National Center for Autonomous Technology (NCAT ATE)",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "PHOTONICS": {
            "production": {
                "LMS_HOST": "photonics.{{ LMS_HOST }}", # "photonics.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.photonics.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.photonics.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                "BADGR_ISSUER_SLUG": "33j37WiUSV-lPUUtht5Pvw",
                "MKG_ROOT_URL": f"photonics.{MKG_HOST}", # "photonics.educateworkforce.com"
            },
            "development": {
                "LMS_HOST": "photonics.{{ LMS_HOST }}",
                "CMS_HOST": "photonics.{{ CMS_HOST }}",
                "MFE_HOST": "apps.photonics.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                "BADGR_ISSUER_SLUG": "I5mydGaQS9KTKNTLQlk7Hw",
                "MKG_ROOT_URL": f"photonics.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - AIM Photonics",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "RECITEXR": {
            "production": {
                "LMS_HOST": "recitexr.{{ LMS_HOST }}", # "recitexr.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.recitexr.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.recitexr.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                # "BADGR_ISSUER_SLUG": "",  # Todo: Need to set this up.
                "MKG_ROOT_URL": f"recitexr.{MKG_HOST}", 
            },
            "development": {
                "LMS_HOST": "recitexr.{{ LMS_HOST }}",
                "CMS_HOST": "recitexr.{{ CMS_HOST }}",
                "MFE_HOST": "apps.recitexr.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                # "BADGR_ISSUER_SLUG": "",
                "MKG_ROOT_URL": f"recitexr.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - RECITEXR",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "REVVED": {
            "production": {
                "LMS_HOST": "revved.{{ LMS_HOST }}", # "revved.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.revved.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.revved.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                # "BADGR_ISSUER_SLUG": "",  # Todo: Need to set this up.
                "MKG_ROOT_URL": f"revved.{MKG_HOST}", 
            },
            "development": {
                "LMS_HOST": "revved.{{ LMS_HOST }}",
                "CMS_HOST": "revved.{{ CMS_HOST }}",
                "MFE_HOST": "apps.revved.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                # "BADGR_ISSUER_SLUG": "",
                "MKG_ROOT_URL": f"revved.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - REVVED",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "REVVED_GVLTEC": {
            "production": {
                "LMS_HOST": "revved-gvltec.{{ LMS_HOST }}", # "revved-gvltec.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.revved-gvltec.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.revved-gvltec.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                # "BADGR_ISSUER_SLUG": "",  # Todo: Need to set this up.
                "MKG_ROOT_URL": f"revved.{MKG_HOST}", 
            },
            "development": {
                "LMS_HOST": "revved-gvltec.{{ LMS_HOST }}",
                "CMS_HOST": "revved-gvltec.{{ CMS_HOST }}",
                "MFE_HOST": "apps.revved-gvltec.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                # "BADGR_ISSUER_SLUG": "",
                "MKG_ROOT_URL": f"revved.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - REVVED - Greenville Technical College",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "REVVED_SCCSC": {
            "production": {
                "LMS_HOST": "revved-sccsc.{{ LMS_HOST }}", # "revved-sccsc.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.revved-sccsc.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.revved-sccsc.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                # "BADGR_ISSUER_SLUG": "",  # Todo: Need to set this up.
                "MKG_ROOT_URL": f"revved.{MKG_HOST}", 
            },
            "development": {
                "LMS_HOST": "revved-sccsc.{{ LMS_HOST }}",
                "CMS_HOST": "revved-sccsc.{{ CMS_HOST }}",
                "MFE_HOST": "apps.revved-sccsc.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                # "BADGR_ISSUER_SLUG": "",
                "MKG_ROOT_URL": f"revved.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - REVVED - Spartanburg Community College",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "REVVED_TRIDENTTECH": {
            "production": {
                "LMS_HOST": "revved-tridenttech.{{ LMS_HOST }}", # "revved-tridenttech.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.revved-tridenttech.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.revved-tridenttech.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                # "BADGR_ISSUER_SLUG": "",  # Todo: Need to set this up.
                "MKG_ROOT_URL": f"revved.{MKG_HOST}", 
            },
            "development": {
                "LMS_HOST": "revved-tridenttech.{{ LMS_HOST }}",
                "CMS_HOST": "revved-tridenttech.{{ CMS_HOST }}",
                "MFE_HOST": "apps.revved-tridenttech.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                # "BADGR_ISSUER_SLUG": "",
                "MKG_ROOT_URL": f"revved.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - REVVED - Trident Technical College",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "SPARTANBURG": {
            "production": {
                "LMS_HOST": "spartanburg.{{ LMS_HOST }}", # "spartanburg.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.spartanburg.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.spartanburg.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                "BADGR_ISSUER_SLUG": "KJ2ni7CaRCe5eWxxj-nUcw",
                "MKG_ROOT_URL": f"spartanburg.{MKG_HOST}", # "spartanburg.educateworkforce.com"
            },
            "development": {
                "LMS_HOST": "spartanburg.{{ LMS_HOST }}",
                "CMS_HOST": "spartanburg.{{ CMS_HOST }}",
                "MFE_HOST": "apps.spartanburg.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                "BADGR_ISSUER_SLUG": "I5mydGaQS9KTKNTLQlk7Hw",
                "MKG_ROOT_URL": f"spartanburg.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - Spartanburg School District",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "THIN_SCHOOL": {
            "production": {
                "LMS_HOST": "thin-school.{{ LMS_HOST }}", # "ts.courses.educateworkforce.com",  # Need to update this to new domain structure `ts.courses.educateworkforce.com`.
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.thin-school.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.thin-school.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                # "BADGR_ISSUER_SLUG": "",
                # "MKG_ROOT_URL": f"thin-school.{MKG_HOST}", 
            },
            "development": {
                "LMS_HOST": "thin-school.{{ LMS_HOST }}",
                "CMS_HOST": "thin-school.{{ CMS_HOST }}",
                "MFE_HOST": "apps.thin-school.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                # "BADGR_ISSUER_SLUG": "",
                "MKG_ROOT_URL": f"thin-school.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - ThinSchool",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "TRUSTWORKS_CYMANII": {
            "production": {
                "BIGCOMMERCE_STORE": "trustworks.cymanii.org",
                "LMS_HOST": "learn.trustworks.cymanii.org", 
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.learn.trustworks.cymanii.org",
                "SESSION_COOKIE_DOMAIN": ".learn.trustworks.cymanii.org", 
                "BADGR_ISSUER_SLUG": "SjuK7cxvS-eCi8h27e1hpQ",
                "MKG_ROOT_URL": f"trustworks.cymanii.org", 
            },
            "development": {
                "BIGCOMMERCE_STORE": "educateworkforce-development.mybigcommerce.com",
                "LMS_HOST": "trustworks-cymanii.{{ LMS_HOST }}",
                "CMS_HOST": "trustworks-cymanii.{{ CMS_HOST }}",
                "MFE_HOST": "apps.trustworks-cymanii.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                "BADGR_ISSUER_SLUG": "equqQ7hdTxGOcLqkz3rHTA",
                "MKG_ROOT_URL": f"trustworks-cymanii.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - TrustWorks-aaS CyManII",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        },
        "WATER_DROPS": {
            "production": {
                "LMS_HOST": "water-drops.{{ LMS_HOST }}", # "water-drops.courses.educateworkforce.com",
                "CMS_HOST": EDUCATEWORKFORCE_CMS_HOST_PROD_DEFAULT,
                "MFE_HOST": "apps.water-drops.{{ EDUCATEWORKFORCE_CONFIG_BASE_DOMAIN }}", # apps.water-drops.educateworkforce.com
                "SESSION_COOKIE_DOMAIN": "{{ EDUCATEWORKFORCE_CONFIG_SESSION_COOKIE_DOMAIN }}",
                # "BADGR_ISSUER_SLUG": "",  # Todo: Need to set this up.
                "MKG_ROOT_URL": f"water-drops.{MKG_HOST}", 
            },
            "development": {
                "LMS_HOST": "water-drops.{{ LMS_HOST }}",
                "CMS_HOST": "water-drops.{{ CMS_HOST }}",
                "MFE_HOST": "apps.water-drops.{{ LMS_HOST }}",
                "SESSION_COOKIE_DOMAIN": "{{ LMS_HOST }}",
                # "BADGR_ISSUER_SLUG": "",
                "MKG_ROOT_URL": f"water-drops.{MKG_HOST}",
            },
            "common": {
                "PLATFORM_NAME": "{{ PLATFORM_NAME }} - REVVED",
                "PRIMARY_COLOR": EDUCATEWORKFORCE_BLUE,
                "FOOTER_NAV_LINKS": [
                    {"title": "Contact", "url": "/contact"},
                ],
                "FOOTER_LEGAL_LINKS": [
                    {"title": "Terms of Service", "url": "/tos"},
                ],
            }
        }
    }
}

########################################
# INITIALIZATION TASKS
########################################

# Initialize for the LMS site configuration settings
hooks.Filters.COMMANDS_INIT.add_items(
    [
        ("lms", ("caregiver", "tasks", "lms", "init")),
        ("lms", ("choose-aerospace", "tasks", "lms", "init")),
        ("lms", ("educateworkforce", "tasks", "lms", "init")),
        ("lms", ("harford-community-college", "tasks", "lms", "init")),
        ("lms", ("meep", "tasks", "lms", "init")),
        ("lms", ("ncatech", "tasks", "lms", "init")),
        ("lms", ("photonics", "tasks", "lms", "init")),
        ("lms", ("recitexr", "tasks", "lms", "init")),
        ("lms", ("revved", "tasks", "lms", "init")),
        ("lms", ("revved-gvltec", "tasks", "lms", "init")),
        ("lms", ("revved-sccsc", "tasks", "lms", "init")),
        ("lms", ("revved-tridenttech", "tasks", "lms", "init")),
        ("lms", ("spartanburg", "tasks", "lms", "init")),
        ("lms", ("thin-school", "tasks", "lms", "init")),
        ("lms", ("trustworks-cymanii", "tasks", "lms", "init")),
        ("lms", ("water-drops", "tasks", "lms", "init")),
    ]
)

########################################
# TEMPLATE RENDERING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

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
        ("recitexr", "build/openedx/themes"),
        ("revved", "build/openedx/themes"),
        ("revved-gvltec", "build/openedx/themes"),
        ("revved-sccsc", "build/openedx/themes"),
        ("revved-tridenttech", "build/openedx/themes"),
        ("spartanburg", "build/openedx/themes"),
        ("thin-school", "build/openedx/themes"),
        ("trustworks-cymanii", "build/openedx/themes"),
        ("water-drops", "build/openedx/themes")
    ],
)

# Copy the SCSS partial files over to the tutor env. It appears this partials directory is 
# ignored by default by tutor/env.py `ENV_PATTERNS_IGNORE`.
hooks.Filters.ENV_PATTERNS_INCLUDE.add_items(
    [
        # Include files from "partials" folders
        r"caregiver/lms/static/sass/partials/lms/theme/",
        r"choose-aerospace/lms/static/sass/partials/lms/theme/",
        r"educateworkforce/lms/static/sass/partials/lms/theme/",
        r"harford-community-college/lms/static/sass/partials/lms/theme/",
        r"indigo/lms/static/sass/partials/lms/theme/",
        r"meep/lms/static/sass/partials/lms/theme/",
        r"ncatech/lms/static/sass/partials/lms/theme/",
        r"photonics/lms/static/sass/partials/lms/theme/",
        r"recitexr/lms/static/sass/partials/lms/theme/",
        r"revved/lms/static/sass/partials/lms/theme/",
        r"revved-gvltec/lms/static/sass/partials/lms/theme/",
        r"revved-sccsc/lms/static/sass/partials/lms/theme/",
        r"revved-tridenttech/lms/static/sass/partials/lms/theme/",
        r"spartanburg/lms/static/sass/partials/lms/theme/",
        r"thin-school/lms/static/sass/partials/lms/theme/",
        r"trustworks-cymanii/lms/static/sass/partials/lms/theme/",
        r"water-drops/lms/static/sass/partials/lms/theme/",
    ]
)

# Load all configuration entries for `indigo`. We don't use this them in production but
# it's here for the plugin and development environment testing.
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"INDIGO_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"INDIGO_{key}", value) for key, value in config["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))


# Load all configuration entries for `caregiver`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"CAREGIVER_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"CAREGIVER_{key}", value) for key, value in config["sites"]["CAREGIVER"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"CAREGIVER_{key}", value) for key, value in config["sites"]["CAREGIVER"]["common"].items()]
)


# Load all configuration entries for `choose-aerospace`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"CHOOSE_AEROSPACE_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"CHOOSE_AEROSPACE_{key}", value) for key, value in config["sites"]["CHOOSE_AEROSPACE"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"CHOOSE_AEROSPACE_{key}", value) for key, value in config["sites"]["CHOOSE_AEROSPACE"]["common"].items()]
)


# Load all configuration entries for `educateworkforce`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"EDUCATEWORKFORCE_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"EDUCATEWORKFORCE_{key}", value) for key, value in config["sites"]["EDUCATEWORKFORCE"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"EDUCATEWORKFORCE_{key}", value) for key, value in config["sites"]["EDUCATEWORKFORCE"]["common"].items()]
)


# Load all configuration entries for `harford-community-college`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"HARFORD_COMMUNITY_COLLEGE_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"HARFORD_COMMUNITY_COLLEGE_{key}", value) for key, value in config["sites"]["HARFORD_COMMUNITY_COLLEGE"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"HARFORD_COMMUNITY_COLLEGE_{key}", value) for key, value in config["sites"]["HARFORD_COMMUNITY_COLLEGE"]["common"].items()]
)


# Load all configuration entries for `meep`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"MEEP_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"MEEP_{key}", value) for key, value in config["sites"]["MEEP"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"MEEP_{key}", value) for key, value in config["sites"]["MEEP"]["common"].items()]
)


# Load all configuration entries for `ncatech`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"NCATECH_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"NCATECH_{key}", value) for key, value in config["sites"]["NCATECH"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"NCATECH_{key}", value) for key, value in config["sites"]["NCATECH"]["common"].items()]
)


# Load all configuration entries for `photonics`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"PHOTONICS_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"PHOTONICS_{key}", value) for key, value in config["sites"]["PHOTONICS"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"PHOTONICS_{key}", value) for key, value in config["sites"]["PHOTONICS"]["common"].items()]
)

# Load all configuration entries for `recitexr`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"RECITEXR_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"RECITEXR_{key}", value) for key, value in config["sites"]["RECITEXR"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"RECITEXR_{key}", value) for key, value in config["sites"]["RECITEXR"]["common"].items()]
)

# Load all configuration entries for `revved`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_{key}", value) for key, value in config["sites"]["REVVED"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_{key}", value) for key, value in config["sites"]["REVVED"]["common"].items()]
)

# Load all configuration entries for `revved-gvltec`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_GVLTEC_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_GVLTEC_{key}", value) for key, value in config["sites"]["REVVED_GVLTEC"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_GVLTEC_{key}", value) for key, value in config["sites"]["REVVED_GVLTEC"]["common"].items()]
)

# Load all configuration entries for `revved-sccsc`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_SCCSC_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_SCCSC_{key}", value) for key, value in config["sites"]["REVVED_SCCSC"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_SCCSC_{key}", value) for key, value in config["sites"]["REVVED_SCCSC"]["common"].items()]
)

# Load all configuration entries for `revved-tridenttech`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_TRIDENTTECH_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_TRIDENTTECH_{key}", value) for key, value in config["sites"]["REVVED_TRIDENTTECH"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"REVVED_TRIDENTTECH_{key}", value) for key, value in config["sites"]["REVVED_TRIDENTTECH"]["common"].items()]
)

# Load all configuration entries for `spartanburg`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"SPARTANBURG_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"SPARTANBURG_{key}", value) for key, value in config["sites"]["SPARTANBURG"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"SPARTANBURG_{key}", value) for key, value in config["sites"]["SPARTANBURG"]["common"].items()]
)


# Load all configuration entries for `thin-school`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"THIN_SCHOOL_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"THIN_SCHOOL_{key}", value) for key, value in config["sites"]["THIN_SCHOOL"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"THIN_SCHOOL_{key}", value) for key, value in config["sites"]["THIN_SCHOOL"]["common"].items()]
)


# Load all configuration entries for `trustworks-cymanii`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"TRUSTWORKS_CYMANII_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"TRUSTWORKS_CYMANII_{key}", value) for key, value in config["sites"]["TRUSTWORKS_CYMANII"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"TRUSTWORKS_CYMANII_{key}", value) for key, value in config["sites"]["TRUSTWORKS_CYMANII"]["common"].items()]
)

# Load all configuration entries for `water-drops`
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"WATER_DROPS_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"WATER_DROPS_{key}", value) for key, value in config["sites"]["WATER_DROPS"][f"{ENVIRONMENT}"].items()]
)
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"WATER_DROPS_{key}", value) for key, value in config["sites"]["WATER_DROPS"]["common"].items()]
)

# Load all patches from the "patches" folder
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutorindigo", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

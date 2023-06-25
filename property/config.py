from django.utils.translation import gettext_lazy as _

CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_ADDITIONAL_FIELDS = {
    "image_field": ["django.forms.ImageField", {"required": False}]
}

CONSTANCE_CONFIG = {
    "SITE_NAME": ("Property App", _("Website title")),
    "SITE_DESCRIPTION": ("", _("Website description")),
    "LOGO_IMAGE": ("", _("Company logo"), "image_field"),
    # Email settings
    "EMAIL": ("admin@example.com", _("Email sender")),
    "APP_PASSWORD": ("123456", _("Sender app password")),
}

CONSTANCE_CONFIG_FIELDSETS = (
    (
        _("General Options"),
        {
            "fields": (
                "SITE_NAME",
                "SITE_DESCRIPTION",
                "LOGO_IMAGE",
            ),
            "collapse": False,
        },
    ),
    (
        _("Email Options"),
        {
            "fields": (
                "EMAIL",
                "APP_PASSWORD",
            ),
            "collapse": True,
        },
    ),
)
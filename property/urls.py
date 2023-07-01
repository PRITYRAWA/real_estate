from django.contrib import admin
from django.urls import path, include
from allauth.socialaccount.views import signup
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        # APPs endpints
        path("foundation/", include("foundation.api.urls", namespace="foundation-api")),
        path("master/", include("api.masters.urls", namespace="masters-api")),
        path(
            "meeting/", include("api.meetings.urls", namespace="meetings-api")
        ),
        path(
            "checkin/", include("api.checkin.urls", namespace="checkin-api")
        ),
        path(
            "task/", include("api.task.urls", namespace="task-api")
        ),
        path(
            "sales/", include("api.sales.urls", namespace="sales-api")
        ),
        path("signup/", signup, name="socialaccount_signup"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

# Schema URLs
urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
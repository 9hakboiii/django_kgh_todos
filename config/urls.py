from django.contrib import admin
from django.urls import path, include

from config import settings

# http://127.0.0.1:8000/admin/
# include ():
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todos.urls")),  # dev_1
]

# dev_3
if settings.DEBUG:
    urlpatterns += [
        path("debug/", include("debug_toolbar.urls")),
    ]

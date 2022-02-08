from django.contrib import admin
from django.urls import path
import jobs.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),
path('home', jobs.views.home, name="home"), ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

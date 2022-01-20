from unicodedata import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from dashboard.settings import MEDIA_ROOT


urlpatterns = [
    path('',views.index,name='index_page')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=MEDIA_ROOT)
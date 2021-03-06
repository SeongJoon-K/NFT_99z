from django.urls import path
from landing import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'landing'

urlpatterns = [
    path("", views.notification, name='home')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
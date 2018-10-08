from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
        url(r'^$',views.index,name='Home'),
        url(r'^new/images$', views.new_image, name='new-image'),
        url(r'^profile/',views.profile, name='profile'),
        url(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

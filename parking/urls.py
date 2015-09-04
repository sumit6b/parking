from django.conf.urls import include, url
from django.contrib import admin
import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'parking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.parkingapp),
    url(r'^$', views.refrence_image, name="refrenceImage"),
    url(r'^$', views.processed_image, name="processedImage")

]

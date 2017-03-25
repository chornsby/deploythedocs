from django.conf.urls import include, url


urlpatterns = [
    url(r'^api/v1/projects/', include('deploythedocs.api.urls', namespace='v1')),
]

from django.conf.urls import url

from deploythedocs.api.views import (
    ProjectsView,
    ProjectVersionsView,
    VersionView,
)


urlpatterns = [
    url(
        r'^$',
        ProjectsView.as_view(),
        name='projects'
    ),
    url(
        r'^(?P<name>[A-Za-z0-9-_.]+)/$',
        ProjectVersionsView.as_view(),
        name='project_versions'
    ),
    url(
        r'^(?P<name>[A-Za-z0-9-_.]+)/(?P<version>[A-Za-z0-9-_.]+)/$',
        VersionView.as_view(),
        name='version'
    ),
]

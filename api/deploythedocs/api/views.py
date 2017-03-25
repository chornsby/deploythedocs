from django.http import Http404
from rest_framework import generics

from deploythedocs.api import serializers, utils
from deploythedocs.api.generics import RetrieveCreateDestroyAPIView


class VersionView(RetrieveCreateDestroyAPIView):
    """Allows modification of a specific version of a specific project."""
    serializer_class = serializers.VersionSerializer

    def get_object(self):
        """Return this version details if it exists else 404."""
        version = utils.try_get_version(self.kwargs['name'], self.kwargs['version'])

        if version:
            return version
        raise Http404

    def perform_create(self, serializer):
        """Create or update the files on disk that match this version."""
        version = serializer.save(**self.kwargs)
        utils.create_or_update(version)

    def perform_destroy(self, version):
        """Remove the files on disk that match this version."""
        utils.destroy(version)


class ProjectVersionsView(generics.ListAPIView):
    """Displays all the versions associated with a specific project."""
    serializer_class = serializers.VerboseVersionSerializer

    def get_queryset(self):
        """Return a list of versions if any exist else 404."""
        documents = utils.list_versions(self.kwargs['name'])

        if documents:
            return documents
        raise Http404


class ProjectsView(generics.ListAPIView):
    """Displays all the documentation hosted on this service."""
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        """Return a list of packages and their versions."""
        return utils.list_all()

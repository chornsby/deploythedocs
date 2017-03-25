from rest_framework import serializers
from rest_framework.reverse import reverse

from deploythedocs.api.models import Version


class VersionSerializer(serializers.ModelSerializer):
    """Serializes a single Version in a minimal format."""
    url = serializers.SerializerMethodField()

    class Meta:
        model = Version
        fields = ('bundle', 'url')
        extra_kwargs = {'bundle': {'write_only': True}}

    def get_url(self, instance):
        """Return an absolute url to where the documentation can be viewed."""
        location = '/%s/%s/index.html' % (instance.name, instance.version)
        return self.context['request'].build_absolute_uri(location)

    def create(self, validated_data):
        """Return a Version instance from submitted data."""
        return Version(**validated_data)


class VerboseVersionSerializer(VersionSerializer):
    """Serializes a single Version in a more verbose format."""
    api = serializers.SerializerMethodField()

    class Meta:
        model = Version
        fields = ('api', 'url', 'version')
        read_only_fields = ('version',)

    def get_api(self, instance):
        """Return an absolute url to the api endpoint for this Version."""
        request = self.context['request']
        kwargs = {'name': instance.name, 'version': instance.version}
        return reverse('version', kwargs=kwargs, request=request)


class ProjectSerializer(serializers.Serializer):
    """Serializes a project and all its Versions in a verbose format."""
    name = serializers.CharField()
    versions = VerboseVersionSerializer(many=True, read_only=True)

    api = serializers.SerializerMethodField()

    def get_api(self, data):
        """Return an absolute url to the api endpoint for this project."""
        request = self.context['request']
        kwargs = {'name': data['name']}
        return reverse('project_versions', kwargs=kwargs, request=request)

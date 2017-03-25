from rest_framework import mixins, generics


class RetrieveCreateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.CreateModelMixin,
                                   mixins.DestroyModelMixin,
                                   generics.GenericAPIView):
    """Custom view to retrieve, create, and destroy all from one endpoint."""
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

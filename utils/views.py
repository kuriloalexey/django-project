from rest_framework.viewsets import GenericViewSet


class BaseViewSet(GenericViewSet):
    """
    GenericViewSet with permissions and serializers by action

    action_serializers = {
        'list': DefaultListSerializer,
    }
    action_permissions = {
        'list': (AllowAny,),
    }
    """

    action_permissions = {}
    action_serializers = {}

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)

    def get_permissions(self):
        permissions = self.action_permissions.get(self.action, self.permission_classes)
        return (permission() for permission in permissions)

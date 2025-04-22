from rest_framework.serializers import ModelSerializers
from core.models import Acessorio

class AcessorioSerializer(ModelSerializers):
    class META:
        model: Acessorio
        fields: "__all__"
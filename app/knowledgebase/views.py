
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models import KnowledgeBase
from knowledgebase import serializers

class KnowledgeBaseViewSet(viewsets.ModelViewSet):
    """ KnowledgeBase view for managing requests """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.KnowledgeBaseDetailsSerializer
    queryset = KnowledgeBase.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.order_by('id')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.KnowledgeBaseSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


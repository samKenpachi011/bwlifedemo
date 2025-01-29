"""
Knowledge base serializer
"""

from rest_framework import serializers
from core.models import KnowledgeBase


#TODO: override create and update functions and handle uploaded files
class KnowledgeBaseSerializer(serializers.ModelSerializer):
    """ KnowledgeBase validations and base list"""

    class Meta:
        model = KnowledgeBase
        fields = ['id', 'knowledge_title', 'content', 'knowledge_category']
        read_only_fields = ['id']

class KnowledgeBaseDetailsSerializer(KnowledgeBaseSerializer):
    """ Details for knowledge base"""

    class Meta(KnowledgeBaseSerializer.Meta):
        fields = KnowledgeBaseSerializer.Meta.fields + ['version', 'document','status','linked_policy']









"""
Test KnowledgeBase Api's
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import KnowledgeBase, Policy, Department


KNOWLEDGE_BASE_URL = reverse('knowledgebase:knowledgebase-list')


def create_kb_document(user, **param):

    defaults = {
        'knowledge_title': 'KB test',
        'content': 'test',
        'version': 'v1.0',
        'knowledge_category': 'general',
        'document_type': 'article',
        'document': 'example2.pdf'}

    dept = Department.objects.create(dept_name="HR")
    policy = Policy.object.create(
        user=user, created_by=user, department=dept,
        title='Test Policy 2',
        description='This is a test policy',
        document='example2.pdf',
        document_type='article')

    kb_obj = KnowledgeBase.objects.create(
        user=user,
        created_by=user,
        department=dept,
        linked_policy=policy,
        **defaults)
    return kb_obj


def details_url(self, kb_id):
    return reverse('knowledgebase:knowledgebase-detail', args=[kb_id])


class PublicKnowledgeBaseTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_unauthorized_access_denied(self):

        res = self.client.get(KNOWLEDGE_BASE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

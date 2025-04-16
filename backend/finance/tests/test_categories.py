import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from finance.models import Category
import uuid

@pytest.fixture
def create_categories():
    category1 = Category.objects.create(name=f"Categoria-{uuid.uuid4()}")
    category2 = Category.objects.create(name=f"Categoria-{uuid.uuid4()}")
    return [category1, category2]

@pytest.mark.django_db
def test_list_categories(create_categories):
    user_model = get_user_model()
    user = user_model.objects.create_user(username="testuser", password="1234")
    
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/finance/categories/")

    assert response.status_code == 200

    category_names = [category["name"] for category in response.data]
    for category in create_categories:
        assert category.name in category_names
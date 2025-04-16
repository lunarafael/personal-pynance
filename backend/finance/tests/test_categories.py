import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from finance.models import Category

@pytest.mark.django_db
def test_list_categories():
    user_model = get_user_model()
    user = user_model.objects.create_user(username="testuser", password="1234")  # Cria um usuário
    client = APIClient()
    client.force_authenticate(user=user)  # Autentica o cliente

    Category.objects.create(name="Educação")
    Category.objects.create(name="Saúde")

    response = client.get("/api/finance/categories/")
    assert response.status_code == 200


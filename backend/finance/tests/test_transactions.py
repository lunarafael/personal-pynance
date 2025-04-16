import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from finance.models import Category

@pytest.fixture
def create_category():
    return Category.objects.create(name="Alimentacao")

@pytest.mark.django_db
def test_create_transaction(create_category):
    user_model = get_user_model()
    user = user_model.objects.create_user(username="testuser", password="1234")

    client = APIClient()
    client.force_authenticate(user=user)

    data = {
        "category": create_category.id,
        "transaction_type": "income",
        "value": 100.00,
        "description": "Salário",
        "date": "2025-04-16",
        "user": user.id
    }

    response = client.post("/api/finance/transactions/", data, format="json")

    assert response.status_code == 201
    assert response.data["value"] == "100.00"
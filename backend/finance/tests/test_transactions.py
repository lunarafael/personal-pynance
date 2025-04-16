import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from finance.models import Category, Transaction

@pytest.mark.django_db
def test_create_transaction():
    user_model = get_user_model()
    user = user_model.objects.create_user(username="testuser", password="1234")
    category = Category.objects.create(name="Alimentacao")

    client = APIClient()
    client.force_authenticate(user=user)

    data = {
        "categoria": category.id,
        "tipo": "income",
        "valor": "100.00",
        "descricao": "Salário",
        "data": "2025-04-16"
    }

    response = client.post("/api/finance/transactions/", data, format="json")
    assert response.status_code == 201
    assert response.data["valor"] == "100.00"

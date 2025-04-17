import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from finance.models import Category
import logging

logger = logging.getLogger(__name__)

@pytest.fixture
def get_existing_category():
    logger.info("Buscando categoria existente para o teste...")
    category = Category.objects.first()
    if not category:
        pytest.fail("Nenhuma categoria foi encontrada no banco de dados. Verifique as migrações ou fixtures.")
    logger.info(f"Categoria utilizada: {category}")
    return category

@pytest.fixture
def auth_client():
    logger.info("Criando usuário e autenticando client...")
    user_model = get_user_model()
    user = user_model.objects.create_user(username="testuser", password="1234")
    client = APIClient()
    client.force_authenticate(user=user)
    logger.info(f"Usuário autenticado: {user.username}")
    return client, user

@pytest.mark.django_db
def test_create_transaction_with_invalid_value(auth_client, get_existing_category):
    logger.info("Iniciando teste de transação com valor inválido...")
    
    client, user = auth_client

    # Valor inválido (negativo)
    data = {
        "category": get_existing_category.id,
        "transaction_type": "income",
        "value": -100.00,
        "desc": "Salário",
        "date": "2025-04-16"
    }

    logger.info(f"Enviando POST com dados inválidos: {data}")
    response = client.post("/api/finance/transactions/", data, format="json")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 400
    assert "value" in response.data
    logger.info("Teste de transação com valor inválido finalizado.")

@pytest.mark.django_db
def test_create_transaction_with_missing_field(auth_client, get_existing_category):
    logger.info("Iniciando teste de transação com campo ausente...")

    client, user = auth_client

    # Campo obrigatório faltando (data)
    data = {
        "category": get_existing_category.id,
        "transaction_type": "income",
        "value": 100.00,
        "desc": "Salário"
    }

    logger.info(f"Enviando POST com dados inválidos (campo ausente): {data}")
    response = client.post("/api/finance/transactions/", data, format="json")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 400
    assert "date" in response.data
    logger.info("Teste de transação com campo ausente finalizado.")
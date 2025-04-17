import pytest
import logging
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from finance.models import Category

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_list_categories():
    logger.info("Iniciando teste de listagem de categorias...")

    user_model = get_user_model()
    user = user_model.objects.create_user(username="testuser", password="1234")
    logger.info(f"Usuário criado: {user.username}")

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/finance/categories/")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 200
    assert isinstance(response.data, list)

    assert len(response.data) > 0
    logger.info(f"Quantidade de categorias retornadas: {len(response.data)}")

    logger.info("Teste de listagem de categorias finalizado com sucesso.")
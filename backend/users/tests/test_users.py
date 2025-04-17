import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)

@pytest.fixture
def auth_client():
    logger.info("Criando usuário e autenticando client...")
    user_model = get_user_model()
    user = user_model.objects.create_user(username="testuser", password="1234")
    client = APIClient()
    client.force_authenticate(user=user)
    logger.info(f"Usuário autenticado: {user.username}")
    return client, user

@pytest.fixture
def staff_auth_client():
    logger.info("Criando usuário staff e autenticando client...")
    user_model = get_user_model()
    staff_user = user_model.objects.create_user(username="staffuser", password="1234")
    staff_user.is_staff = True
    staff_user.save()
    client = APIClient()
    client.force_authenticate(user=staff_user)
    logger.info(f"Usuário staff autenticado: {staff_user.username}")
    return client, staff_user

@pytest.mark.django_db
def test_create_user():
    logger.info("Iniciando teste de criação de usuário...")
    
    client = APIClient()
    
    data = {
        "username": "newuser",
        "password": "password123",
        "email": "newuser@example.com"
    }

    logger.info(f"Enviando POST com dados: {data}")
    response = client.post("/api/users/register/", data, format="json")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")
    
    assert response.status_code == 201
    assert response.data["username"] == data["username"]
    assert "password" not in response.data
    logger.info("Teste de criação de usuário finalizado com sucesso.")

@pytest.mark.django_db
def test_create_user_with_missing_field():
    logger.info("Iniciando teste de criação de usuário com campo ausente...")

    client = APIClient()
    
    # Enviando dados incompletos (faltando password)
    data = {
        "username": "invaliduser",
        "email": "invaliduser@example.com"
    }

    logger.info(f"Enviando POST com dados inválidos: {data}")
    response = client.post("/api/users/register/", data, format="json")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 400
    assert "password" in response.data
    logger.info("Teste de criação de usuário com campo ausente finalizado.")

@pytest.mark.django_db
def test_login_user(auth_client):
    logger.info("Iniciando teste de login de usuário...")

    client, user = auth_client
    
    data = {
        "username": "testuser",
        "password": "1234"
    }
    
    logger.info(f"Enviando POST com dados de login: {data}")
    response = client.post("/api/token/", data, format="json")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 200
    assert "access" in response.data
    logger.info("Teste de login de usuário finalizado com sucesso.")

@pytest.mark.django_db
def test_login_user_with_invalid_credentials():
    logger.info("Iniciando teste de login com credenciais incorretas...")

    client = APIClient()
    
    # Enviando credenciais incorretas
    data = {
        "username": "testuser",
        "password": "wrongpassword"
    }

    logger.info(f"Enviando POST com dados de login incorretos: {data}")
    response = client.post("/api/token/", data, format="json")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 401
    assert "detail" in response.data
    logger.info("Teste de login com credenciais incorretas finalizado.")


@pytest.mark.django_db
def test_list_users_with_staff_permission(staff_auth_client):
    logger.info("Iniciando teste de listagem de usuários com permissão de staff...")

    client, user = staff_auth_client

    response = client.get("/api/users/list/")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 200
    assert isinstance(response.data, list)
    logger.info("Teste de listagem de usuários com permissão de staff finalizado com sucesso.")

@pytest.mark.django_db
def test_list_users_without_authentication():
    logger.info("Iniciando teste de listagem de usuários sem autenticação...")

    client = APIClient()

    response = client.get("/api/users/list/")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 401
    logger.info("Teste de listagem de usuários sem autenticação finalizado com sucesso.")

@pytest.mark.django_db
def test_list_users_without_staff_permission(auth_client):
    logger.info("Iniciando teste de listagem de usuários sem permissão de staff...")

    client, user = auth_client

    response = client.get("/api/users/list/")
    logger.info(f"Resposta recebida: {response.status_code} - {response.data}")

    assert response.status_code == 403
    logger.info("Teste de listagem de usuários sem permissão de staff finalizado com sucesso.")
from django.urls import path
from .views import CategoryListView, TransactionListCreateView, TransactionDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'), # GET /api/finance/categories/
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'), # GET/POST /api/finance/transactions/ and POST /api/finance/transactions/
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'), # GET/POST /api/finance/transactions/<id>/, PUT /api/finance/transactions/<id>/, DELETE /api/finance/transactions/<id>/
]
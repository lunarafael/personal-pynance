from django.urls import path
from .views import CategoryListView, TransactionListCreateView, TransactionDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list-create'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
]
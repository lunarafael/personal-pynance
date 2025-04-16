from django.urls import path
from .views import CategoryListCreateView, TransactionListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
]
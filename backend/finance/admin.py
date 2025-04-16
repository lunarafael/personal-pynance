from django.contrib import admin
from .models import Transaction, Category

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'category', 'transaction_type', 'value', 'desc', 'date')
    search_fields = ('transaction_id', 'user__username', 'category__name', 'transaction_type')
    list_filter = ('transaction_type', 'category')

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category)

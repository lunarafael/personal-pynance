from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50, default='Outros')
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    transaction_id = models.AutoField(
        primary_key=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, 
        null=True, 
        blank=False
    )
    transaction_type = models.CharField(
        max_length=10, 
        choices=TYPE_CHOICES
    )
    value = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        blank=False, 
        null=False, 
        validators=[MinValueValidator(0)]
    )
    desc = models.CharField(
        max_length=255, 
        blank=True
    )
    date = models.DateField()

    def __str__(self):
        return f"ID: {self.transaction_id} - User: {self.user.username} - Type: {self.transaction_type} - Value: {self.value} - Date: {self.date}"
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.name == 'finance':
        default_categories = [
            "Educação", "Entretenimento", "Alimentação",
            "Transporte", "Saúde", "Estética", "Contas", "Outros"
        ]
        for name in default_categories:
            slug = slugify(name)
            Category.objects.get_or_create(name=name, slug=slug)
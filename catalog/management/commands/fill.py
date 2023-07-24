from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **option):
        category_list = [
            {'name': 'Смартфоны', 'description': 'Смартфоны и планшеты'},
            {'name': 'Всё для сада', 'description': 'Инструменты, семена, развлечения и украшения'},
            {'name': 'Бытовая техника', 'description': 'Всё для дома'},
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)

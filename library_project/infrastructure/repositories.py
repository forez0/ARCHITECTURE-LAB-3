# infrastructure/repositories.py
from django.apps import apps


BookModel = apps.get_model('adapters', 'BookModel')
OrderModel = apps.get_model('adapters', 'OrderModel')

Book = apps.get_model('domain', 'Book')

class DjangoRepository:
    def get_all_books(self):
        return [Book(id=b.id, title=b.title, author=b.author) for b in BookModel.objects.all()]

    def save_order(self, user_id, book_id):
        OrderModel.objects.create(user_id=user_id, book_id=book_id)

    def get_user_orders(self, user_id):
        return BookModel.objects.filter(ordermodel__user_id=user_id)

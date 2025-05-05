# domain/services.py
def order_book(user, book, repository):
    repository.save_order(user.id, book.id)

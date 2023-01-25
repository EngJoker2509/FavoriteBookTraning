from django.db import models
from myapp.models import *

# liked_books = a list of books a given user likes
# books_uploaded = a list of books uploaded by a given user


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(
        User, related_name='books', on_delete=models.CASCADE)
    favorite_book = models.ManyToManyField(User, related_name='favorites')

    def create_book(request):
        _title = request.POST['title']
        _desc = request.POST['desc']
        id = request.session['userid']
        _user = User.objects.get(id=id)
        Book.objects.create(title=_title, desc=_desc, uploaded_by=_user)

    def assign_user_to_book(user_id, book_id):
        _user_id = User.objects.get(id=user_id)
        _book_id = Book.objects.get(id=book_id)
        # _user_id.favorites.add(_book_id)
        _book_id.favorite_book.add(_user_id)

    def get_all_books():
        return Book.objects.all()

    def get_book_by_id(id):
        return Book.objects.get(id=id)

  # uploaded_by = user who uploaded a given book
  # users_who_like = a list of users who like a given book

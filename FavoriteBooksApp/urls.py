from django.urls import path
from . import views

app_name = 'FavoriteBooksApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('destroy', views.destroy, name='destroy'),
    path('book/<int:id>', views.books, name='books'),
    path('addbooks/<int:id>',views.addbooks,name='addbooks'),
]

from django.urls import path

from applications.books.views import BookListView

urlpatterns = [
    path('books-list/', BookListView.as_view()),
]
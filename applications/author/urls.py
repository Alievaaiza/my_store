from django.urls import path

from applications.author.views import AuthorListView

urlpatterns = [
    # 1
    # path('authors-list/', author_list),
    # 2
    # path('authors-list/', AuthorView.as_view()),
    # 3
    path('authors-list/', AuthorListView.as_view()),
]
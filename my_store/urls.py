
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('applications.author.urls')),
    path('books/', include('applications.books.urls')),
]

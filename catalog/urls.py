from django.urls import path
from . import views
from django.conf.urls import url


"""
URL addresses for this site
catalog/                    main page
catalog/books/              books list
catalog/authors/            authors list
catalog/book/<id>           book detail info
catalog/author/<id>         author detail info
"""


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^books/$',views.BookListView.as_view(), name='books'),
    url(r'^book/<id>$', views.BookDetailView.as_view(), name='book-detail'),
        ]

from django.urls import path
from . import views


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
        ]

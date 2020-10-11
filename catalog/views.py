from django.shortcuts import render
from .models import *


def index(request):
    """
    Function that represent main page of the site
    """

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # show avaliable books with status 'a'
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    return render(
            request,
            'index.html',
            context={
                'num_books':num_books,
                'num_instances':num_instances,
                'num_instances_available':num_instances_available,
                'num_authors':num_authors,
                }
            )

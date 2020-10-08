from django.db import models

class Genre(models.Model):
    """
    Model representing a book genre 
    """

    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        """
        String for representing the Model object in Views
        """

        return self.name


class Book(model.Models):
    """
    Model representing a book
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Characters code of the book')
    genre = molels.ManyToManyField(Genre, help_text='Select a gere for this book')

    def __str__(self):
        """
        String for representing the Model object in Views
        """

        return self.title



from django.db import models
from django.urls import reverse
import uuid

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


class Book(models.Model):
    """
    Model representing a book
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter\
                                                           a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Characters code of the book')
    genre = models.ManyToManyField(Genre, help_text='Select a gere for this book')
    language = models.ForeignKey('Language', verbose_name='Original language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object in Views
        """

        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance
        """

        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display
        related Genre strings
        """
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'


class Author(models.Model):
    """
    Model representing an author of book
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Born', null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance
        """

        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """

        return '%s, %s' % (self.last_name, self.first_name)


class BookInstance(models.Model):
    """
    Model representing a specific copy of the book, that can be borrowed from the library
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for book')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
            ('m', 'Maintenance'),
            ('o', 'On loan'),
            ('a', 'Available'),
            ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a')


    class Meta:
        """
        Meta class for manage BookInstance behavior
        """

        ordering = ['due_back']

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.book.title)

class Language(models.Model):
    """
    Model representing language of the book
    """

    lang = models.CharField('Language', max_length=50)

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.lang

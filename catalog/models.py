from django.db import models
from django.urls import reverse
# Create your models here.
import uuid


class Genre(models.Model):
    """Genre model"""
    name = models.CharField(max_length=200, help_text='Help text goes here')
    def __str__(self):
        """Return str repr"""
        return self.name

class Book(models.Model):
    """Book model"""
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Help text for a book')

    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='Help text for isbn..<a href="https://lmgtfy.com/isb>What?></a>')

    def __str__(self):
            """String repr"""
            return self.title

    def get_absolute_url(self):
            return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id help text')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Author repr"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Abs url"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """Str repr"""
        return f'{self.last_name}, {self.first_name}'
        


from django.db import models

# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class SchoolClass(models.Model):
    class_name = models.CharField(max_length=12)
    class_master = models.CharField(max_length=12)

    def __str__(self):
        return '<SchoolClass: {0}>'.format(self.class_name)

    __unicode__ = __str__

class Student(models.Model):
    school_class = models.ForeignKey(SchoolClass,on_delete=models.CASCADE)
    name = models.CharField(max_length=12)

class Author(models.Model):
    author_name = models.CharField(max_length=24)

class Book(models.Model):
    book_name = models.CharField(max_length=48)
    authors = models.ManyToManyField(Author)
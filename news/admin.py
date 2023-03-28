from django.contrib import admin
from . import models
from .models import Student, SchoolClass, Book, Author

# Register your models here.
admin.site.register(models.Article)
admin.site.register(Student)
admin.site.register(SchoolClass)
admin.site.register(Author)
admin.site.register(Book)
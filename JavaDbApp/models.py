from django.db import models

# Create your models here.

class Author(models.Model):
     name = models.CharField(max_length=30)
     email = models.EmailField()

     def __str__(self):
         return self.name

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





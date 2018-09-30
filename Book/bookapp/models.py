from django.db import models
from django.contrib.auth.models import User
# 1 alwyas refers to Yes and O always refers to No.

class Sell_book(models.Model):
    baragain_choice = (
        ('YES', 'YES'),
        ('NO','NO'),
        )

    date = models.DateField(auto_now_add=True)
    book_title = models.CharField(max_length=100)
    isbn_no = models.CharField(max_length=20)
    author = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()
    negotiable = models.CharField(max_length=3, choices=baragain_choice)
    description = models.CharField(max_length=2000)
    photo = models.ImageField(upload_to="photo", blank="True")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.isbn_no
    
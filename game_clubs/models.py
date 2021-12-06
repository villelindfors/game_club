from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Game(models.Model):

    name = models.CharField(max_length=200)
    maker = models.JSONField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.name} by {',' .join(self.maker)}."

class Review(models.Model):

    my_review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.my_review[:50]}..."

class Loan(models.Model):

    my_loan = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.my_loan[:50]}..."
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treatment(models.Model):
    treatment = models.CharField(max_length = 200)
    class Meta:
        ordering = ["treatment"]
    
    def __str__(self):
        return str(self.id) + "-" + self.treatment

class Article (models.Model):
    title = models.CharField(max_length = 400)
    author = models.CharField(max_length = 400)
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='articles', null=True, blank = True)
    processed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.id) + "-" + self.title

class Context (models.Model):
    context = models.TextField()
    
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    article = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + "-" + self.paper.title 

class Question (models.Model):
    question = models.TextField()
    answer = models.TextField(max_length = 500, null=True, blank=True)

    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + "-" + self.question


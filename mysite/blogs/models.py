from django.db import models

class Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title_text

class Content(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    content_text = models.CharField(max_length=2000)
    def __str__(self):
        return self.content_text
# Create your models here.

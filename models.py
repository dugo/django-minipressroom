from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=1,unique=True)

    class Meta:
        ordering = ('order',)

class News(models.Model)
    section = models.ForeignKey(Section)
    title = models.CharField(max_length=1024)
    date = models.DateField()
    link = models.URLField()
    image = models.ImageField(upload_to="images/")
    
    class Meta:
        ordering = ('-date',)

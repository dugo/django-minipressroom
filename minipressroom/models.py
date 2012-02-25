from django.db import models
from django.conf import settings
from tinymce import models as tinymce_models
from transmeta import TransMeta
from django.utils.translation import get_language


class Section(models.Model):
    __metaclass__ = TransMeta
    name = models.CharField("name",max_length=100)
    order = models.PositiveIntegerField(default=1,unique=True)

    def get_news(self):
        return self.news.filter(lang=get_language)
    
    @classmethod
    def get_all(self):
        return self.objects.all()

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('order',)
        translate = ('name',)

class News(models.Model):
    section = models.ForeignKey(Section,related_name="news")
    title = models.CharField(max_length=1024)
    date = models.DateField()
    link = models.URLField(max_length=1024,blank=True)
    image = models.ImageField(upload_to="minipressroom/",blank=True)
    abstract = models.TextField(blank=True,default="")
    lang = models.CharField(max_length=2,choices=settings.LANGUAGES,default=settings.LANGUAGE_CODE)
    
    @classmethod
    def get_for_lang(self,lang):
        return self.objects.filter(lang=lang)
    
    def __unicode__(self):
        return unicode(self.title)
    
    class Meta:
        ordering = ('section','-date',)

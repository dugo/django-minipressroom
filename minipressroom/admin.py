import models
from django.contrib import admin


class Section(admin.ModelAdmin):
    model = models.Section
    list_display = ("__unicode__","order",)

def make_set_section(section):
    def set_section(self,request, queryset):
        queryset.update(section=section)

    return set_section


customactions = []

for s in models.Section.objects.all():
    act = make_set_section(s)
    act.__name__ = "set_section_%d" % s.id
    act.short_description = "Set selected in the %s section" % s
    customactions.append(act)

class News(admin.ModelAdmin):
    model = models.News
    search_fields = ("title",)
    list_display = ("__unicode__","section","lang","date","enlace",)
    list_filter = ("section","lang",)
    
    def enlace(self,o):
        return "<a href='%(link)s' target='_blank'>%(link)s</a>" % dict(link=o.link)
    enlace.allow_tags=True
    
    actions = customactions


admin.site.register(models.Section,Section)
admin.site.register(models.News,News)

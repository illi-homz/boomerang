from django.contrib import admin
from . import models

# admin.site.register(models.New)
# admin.site.register(models.Service)
# admin.site.register(models.Stock)
admin.site.register(models.Article)
admin.site.register(models.Document)
admin.site.register(models.Photo)
admin.site.register(models.Client)
admin.site.register(models.Feedback)
admin.site.register(models.Link)


def dublicate_ad(modeladmin, request, queryset):
	#клонирование выбранных Ad
	for el in queryset:
		el.pk = None
		el.save()

dublicate_ad.short_description = "Дублировать объект"

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
	actions = [dublicate_ad]

@admin.register(models.New)
class NewAdmin(admin.ModelAdmin):
	actions = [dublicate_ad]

@admin.register(models.Stock)
class StockAdmin(admin.ModelAdmin):
	actions = [dublicate_ad]

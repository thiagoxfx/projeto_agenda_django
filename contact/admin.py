from contact import models
from django.contrib import admin


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show',)
    ordering = ('-id',)
    search_fields = ('id', 'first_name', 'last_name',)
    # list_filter = ('create_date',)
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('first_name', 'last_name', 'show')
    list_display_links = ('id', 'phone',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name'),
    ordering = ('id'),

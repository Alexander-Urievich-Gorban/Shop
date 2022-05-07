from django.contrib import admin
from django import forms

from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "id", "get_image")
    list_filter = ["category", ]
    search_fields = ("title", "category__title")
    readonly_fields = ("get_image",)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="300" height="350"')

    get_image.short_description = "Изображение"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "get_image")
    list_filter = ["title", ]
    readonly_fields = ("get_image",)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="300" height="250"')

    get_image.short_description = "Изображение"


@admin.register(Basket)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("product", "count_products")

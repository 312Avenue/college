from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Content, Img, File, Comment


class ImgItemsLine(admin.TabularInline):
    model = Img
    extra = 0
    readonly_fields = ('icon_tag',)

    def icon_tag(self, obj):
        if not (obj.pk and obj.img):
                return 'Нет фото'
        return mark_safe('<img src="%s" width=100/>' % obj.img.url)
    icon_tag.short_description = 'img'
    icon_tag.allow_tags = True


class FileItemsLine(admin.TabularInline):
    model = File
    extra = 0


class ImgAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [ImgItemsLine, FileItemsLine]
    readonly_fields = ('icon_tag',)

    def icon_tag(self, obj):
        if not (obj.pk and obj.img):
                return 'Нет фото'
        return mark_safe('<img src="%s" width=100/>' % obj.img.url)
    icon_tag.short_description = 'img'
    icon_tag.allow_tags = True


admin.site.register(Content, ImgAdmin)
admin.site.register(Comment)

from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
     # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'
    list_editable = ('group',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-empty-'

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
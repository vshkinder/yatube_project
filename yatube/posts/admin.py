from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('text', 'pub_date', 'author')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)

# При регистрации модели Post источником конфигурации для неё назначаем


# класс PostAdmin
admin.site.register(Post, PostAdmin)

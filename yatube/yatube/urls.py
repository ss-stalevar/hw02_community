from django.conf import settings
# anfisa/urls.py (главный файл url проекта)
# По умолчанию в проект Django подключена система администрирования
from django.contrib import admin
# Функция include позволит использовать path() из других файлов.
# Импортируем!
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls', namespace='about')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
]

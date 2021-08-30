from django.shortcuts import render

# Create your views here.


def index(request):
    template = 'posts/group_list.html'
    context = {
        'text': 'Записи сообщества',
        'main': 'Информация Б на странице группы будет тут.'
    }
    return render(request, template, context)

from django.http import HttpResponse


def group_posts(request, slug):
    return HttpResponse('Страница, на которой будут посты, отфильтрованные по группам.')

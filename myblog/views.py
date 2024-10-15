from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# def post_list(request):  # без выбора количества постов на странице
#     post_list = Post.objects.all().order_by('-pub_date')
#     paginator = Paginator(post_list, 3)  # Показывать 3 поста на странице
#
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # Если страница не является целым числом, то показываем первую страницу.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # Если страница больше максимальной, то показываем последнюю страницу результатов.
#         posts = paginator.page(paginator.num_pages)
#
#     return render(request, 'blog/post_list.html', {'posts': posts})

def post_list(request):  # для выбора количества постов на странице
    post_list = Post.objects.all().order_by('-pub_date')

    # Получаем количество элементов на странице из GET-параметра
    items_per_page = request.GET.get('items', 3)
    try:
        items_per_page = int(items_per_page)
    except ValueError:
        items_per_page = 3

    paginator = Paginator(post_list, items_per_page)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'myblog/post_list.html', {'posts': posts, 'items_per_page': items_per_page})

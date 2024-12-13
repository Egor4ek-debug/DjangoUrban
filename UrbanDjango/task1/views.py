from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Buyer, Game, News
from .forms import UserRegister

text_all_button = 'Back to main page'
main_page = 'Main page'
second_page = 'Store'
third_page = 'Cart'


def menu(request):
    context = {
        'main_page': main_page,
        'second_page': second_page,
        'third_page': third_page

    }
    return render(request, 'fourth_task/menu.html', context)


def store(request):
    store_h1 = 'Store Games'
    text_button = 'Buy'
    games = Game.objects.all()
    context = {
        'store_h1': store_h1,
        'text_button': text_button,
        'text_all_page': text_all_button,
        'main_page': main_page,
        'second_page': second_page,
        'third_page': third_page,
        'games': games  # Передача коллекции игр в контекст
    }
    return render(request, 'fourth_task/store.html', context)


def cart(request):
    store_h1 = 'Cart'
    text = 'Sorry, you cart is empty'

    context = {
        'store_h1': store_h1,
        'text': text,
        'text_all_page': text_all_button,
        'main_page': main_page,
        'second_page': second_page,
        'third_page': third_page
    }
    return render(request, 'fourth_task/cart.html', context)


# Create your views here.


# users = ["user1", "test_user", "admin"]


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
            users = Buyer.objects.values_list('name', flat=True)
            if username in users:
                info["error"] = "Пользователь уже существует"
            elif password != repeat_password:
                info["error"] = "Пароли не совпадают"
            elif age < 18:
                info["error"] = "Вы должны быть старше 18"
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info["success"] = f"Приветствуем, {username}!"
        else:
            info["error"] = "Форма заполнена некорректно"
    else:
        form = UserRegister()

    info["form"] = form
    return render(request, "fifth_task/registration_page.html", info)


# def sign_up_by_html(request):
#     info = {}
#     if request.method == "POST":
#         username = request.POST.get("username", "").strip()
#         password = request.POST.get("password", "").strip()
#         repeat_password = request.POST.get("repeat_password", "").strip()
#         age = request.POST.get("age", "").strip()
#
#         if not username or len(username) > 30:
#             info["error"] = "Некорректный логин"
#         elif username in users:
#             info["error"] = "Пользователь уже существует"
#         elif password != repeat_password:
#             info["error"] = "Пароли не совпадают"
#         elif not age.isdigit() or int(age) < 18:
#             info["error"] = "Вы должны быть старше 18"
#         else:
#             users.append(username)
#             info["success"] = f"Приветствуем, {username}!"
#
#     return render(request, "UrbanDjango/templates/fifth_task/registration_page.html", info)

def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    return render(request, 'platform/news.html', {'news': news_page})

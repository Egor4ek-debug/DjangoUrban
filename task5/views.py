from django.shortcuts import render
from .forms import UserRegister

users = ["user1", "test_user", "admin"]


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if username in users:
                info["error"] = "Пользователь уже существует"
            elif password != repeat_password:
                info["error"] = "Пароли не совпадают"
            elif age < 18:
                info["error"] = "Вы должны быть старше 18"
            else:
                users.append(username)
                info["success"] = f"Приветствуем, {username}!"
        else:
            info["error"] = "Форма заполнена некорректно"
    else:
        form = UserRegister()

    info["form"] = form
    return render(request, "fifth_task/registration_page.html", info)


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        repeat_password = request.POST.get("repeat_password", "").strip()
        age = request.POST.get("age", "").strip()

        if not username or len(username) > 30:
            info["error"] = "Некорректный логин"
        elif username in users:
            info["error"] = "Пользователь уже существует"
        elif password != repeat_password:
            info["error"] = "Пароли не совпадают"
        elif not age.isdigit() or int(age) < 18:
            info["error"] = "Вы должны быть старше 18"
        else:
            users.append(username)
            info["success"] = f"Приветствуем, {username}!"

    return render(request, "fifth_task/registration_page.html", info)

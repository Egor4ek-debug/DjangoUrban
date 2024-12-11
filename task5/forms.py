from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин:",
        widget=forms.TextInput(attrs={"placeholder": "Логин", "maxlength": "30"})
    )
    password = forms.CharField(
        min_length=8,
        label="Введите пароль:",
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"})
    )
    repeat_password = forms.CharField(
        min_length=8,
        label="Повторите пароль:",
        widget=forms.PasswordInput(attrs={"placeholder": "Повтор пароля"})
    )
    age = forms.IntegerField(
        min_value=18,
        max_value=120,
        label="Введите свой возраст:",
        widget=forms.NumberInput(attrs={"placeholder": "Возраст"})
    )

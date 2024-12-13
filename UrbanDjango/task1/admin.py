from django.contrib import admin
from .models import Game, Buyer


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')  # Фильтрация по полям size, cost

    list_display = ('title', 'cost', 'size')  # Отображение полей title,cost,size

    search_fields = ('title',)  # Поиск по полю title

    list_per_page = 20  # ограничение на количество записей 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')

    list_display = ('name', 'balance', 'age')

    search_fields = ('name',)

    list_per_page = 30

    readonly_fields = ('balance',)

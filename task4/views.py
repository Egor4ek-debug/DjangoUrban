from django.shortcuts import render

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
    store_h1 = 'Store sneakers'
    text_button = 'Add to cart'
    url_images = [
        "https://funkydunky.ru/upload/iblock/46a/vugbuybdqntf8wocvazy18jslfxoxdfb.jpg",
        "https://funkydunky.ru/upload/iblock/b21/my701ytsun45p1jg3ptbfj12mlnhezsm.jpg",
        "https://funkydunky.ru/upload/iblock/c38/0pd0apwc10vgyrsap2243i7lwii0el6g.jpg"
    ]
    shoes = ['Giannis Immortality 4, Humility', 'LeBron Witness VIII, Armoury Navy', 'Jordan Point Lane, Cool Grey']

    combined = zip(url_images, shoes)
    context = {
        'store_h1': store_h1,
        'text_button': text_button,
        'text_all_page': text_all_button,
        'main_page': main_page,
        'second_page': second_page,
        'third_page': third_page,
        'combined': combined
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

from django.shortcuts import render

text_all_button = 'Back to main page'


def main_page(request):
    main_page = 'Main page'
    second_page = 'Store'
    third_page = 'Cart'
    context = {
        'main_page': main_page,
        'second_page': second_page,
        'third_page': third_page

    }
    return render(request, 'third_task/main.html', context)


def second_page(request):
    store_h1 = 'Store sneakers'
    shoes_1 = 'Giannis Immortality 4, Humility'
    shoes_2 = 'LeBron Witness VIII, Armoury Navy'
    shoes_3 = 'Jordan Point Lane, Cool Grey'

    text_button = 'Add to cart'
    context = {
        'store_h1': store_h1,
        'shoes_1': shoes_1,
        'shoes_2': shoes_2,
        'shoes_3': shoes_3,
        'text_button': text_button,
        'text_all_page': text_all_button

    }
    return render(request, 'third_task/store.html', context)


def third_page(request):
    store_h1 = 'Cart'
    text = 'Sorry, you cart is empty'

    text_button = 'Back'
    context = {
        'store_h1': store_h1,
        'text': text,
        'text_all_page': text_all_button
    }
    return render(request, 'third_task/cart.html', context)
# Create your views here.

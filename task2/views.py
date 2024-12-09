from django.shortcuts import render


def func_template(request):
    return render(request, 'second_task/func_template.html')
# Create your views here.

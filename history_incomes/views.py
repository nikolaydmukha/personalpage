from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'history_incomes/history_incomes.html')

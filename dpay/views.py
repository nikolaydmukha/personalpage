from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"active": "dpay", "title": "Обещанный платёж"}
    return render(request, 'dpay/dpay.html', context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {"active": "dpay", "title": "Обещанный платёж"}
    return render(request, 'dpay/dpay.html', context)

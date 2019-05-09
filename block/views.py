from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "block", "title": "Добровольная блокировка доступа"}
    return render(request, 'block/block.html', context)

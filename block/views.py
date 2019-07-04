from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {"active": "block", "title": "Добровольная блокировка доступа"}
    return render(request, 'block/block.html', context)

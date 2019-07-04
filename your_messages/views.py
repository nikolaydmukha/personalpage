from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {"active": "your_messages", "title": "Мои сообщения"}
    return render(request, 'messages/messages.html', context)

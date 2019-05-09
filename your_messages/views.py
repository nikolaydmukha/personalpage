from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "your_messages", "title": "Мои сообщения"}
    return render(request, 'messages/messages.html', context)

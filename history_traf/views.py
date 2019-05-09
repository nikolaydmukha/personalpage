from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "history_traf", "title": "Расходы и трафик"}
    return render(request, 'history_traf/history_traf.html', context)

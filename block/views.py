from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {
        "active": "block",
        "title": "Добровольная блокировка доступа",
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data']
    }
    return render(request, 'block/block.html', context)

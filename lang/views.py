from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def home(request):
    # trans = translate(language='fr')
    return render(request, 'home.html')
    #, {'trans': trans})

def item(request):
    context = {'items': Item.objects.all()}
    return render(request, 'item.html', context=context)
    #, {'trans': trans})


def update_timezone(request):
    selected_timezone = request.POST.get('selected_timezone')
    request.user.profile.timezone = selected_timezone
    request.user.profile.save()
    # return redirect(request.path)
    return JsonResponse({'result': 'success'})
# def translate(language):
#     cur_language = get_language()
#     try:
#         activate(language)
#         text = gettext('hello')
#     finally:
#         activate(cur_language)
#     return text
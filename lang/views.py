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
    return JsonResponse({'result': 'success'})


def create_post(request):
    post_content = request.POST.get('data_item[post_content]')
    p = Post(text_content=post_content)  # Creating Like Object
    p.save()  # saving it to store in database
    data = {
             'result': True,
             'post':{
                        'text_content': p.text_content,
                        }
           }
    return JsonResponse(data)


def test_page(request):
    return render(request, 'test_page.html')









# def translate(language):
#     cur_language = get_language()
#     try:
#         activate(language)
#         text = gettext('hello')
#     finally:
#         activate(cur_language)
#     return text
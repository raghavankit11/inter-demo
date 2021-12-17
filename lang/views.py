from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView

from .models import *
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


def home(request):
    # trans = translate(language='fr')
    return render(request, 'home.html')
    # , {'trans': trans})


def item(request):
    context = {'items': Item.objects.all()}
    return render(request, 'item.html', context=context)
    # , {'trans': trans})


def items(request):
    context = {'items': Item.objects.all()}
    return render(request, 'items/items.html', context=context)


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
        'post': {
            'text_content': p.text_content,
        }
    }
    return JsonResponse(data)


def test_page(request):
    return render(request, 'test_page.html')


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item

    def get_object(self, queryset=None):
        obj = super(PostDetailView, self).get_object()
        user = self.request.user
        obj.is_user_subscribed = obj.subscriptions.filter(user__id__exact=user.id).exists()
        obj.is_user_subscribed_not = not obj.is_user_subscribed
        return obj


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'amount', 'quantity']
    template_name = 'Items/AddItem.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lang:items')


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'amount', 'quantity']

    def form_valid(self, form):
        return super().form_valid(form)

# def item_add(request):
#     context = {}
#     return render(request, 'item.html', context=context)
#     #, {'trans': trans})


# def translate(language):
#     cur_language = get_language()
#     try:
#         activate(language)
#         text = gettext('hello')
#     finally:
#         activate(cur_language)
#     return text

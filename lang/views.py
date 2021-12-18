from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import LoginForm
from .models import *
from django.contrib.auth import authenticate, logout as django_logout, login as django_login

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def item(request):
    context = {'items': Item.objects.all()}
    return render(request, 'item.html', context=context)

@login_required
def items(request):
    context = {'items': Item.objects.all()}
    return render(request, 'items/items.html', context=context)

@login_required
def update_timezone(request):
    selected_timezone = request.POST.get('selected_timezone')
    request.user.profile.timezone = selected_timezone
    request.user.profile.save()
    return JsonResponse({'result': 'success'})

@login_required
def create_post(request):
    post_content = request.POST.get('data_item[post_content]')
    p = Post(text_content=post_content)
    p.save()
    data = {
        'result': True,
        'post': {
            'text_content': p.text_content,
        }
    }
    return JsonResponse(data)

@login_required
def test_page(request):
    return render(request, 'test_page.html')


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'amount', 'quantity']
    template_name = 'Items/AddItem.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lang:items')

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item

    def get_object(self, queryset=None):
        obj = super(ItemDetailView, self).get_object()
        user = self.request.user
        obj.is_user_subscribed = obj.subscriptions.filter(user__id__exact=user.id).exists()
        obj.is_user_subscribed_not = not obj.is_user_subscribed
        return obj


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'amount', 'quantity']

    def form_valid(self, form):
        return super().form_valid(form)

def login(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}

    if request.method == "POST":
        username = request.POST['username']
        if 'sign-in' in request.POST:
            password = request.POST['password']

            # check if user has entered correct credentials
            user = authenticate(username=username, password=password)

            if user is not None and user.is_authenticated:
                django_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # django_login(request, user)
                return redirect('lang:items')
            else:
                return render(request, 'lang/login.html', context=context)

    return render(request, 'lang/login.html', context=context)

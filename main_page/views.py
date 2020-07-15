from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import ListView
from .serializers import MainListSerializer

from .forms import AddForm
from .models import Main


class MainListView(APIView):
    def get(self, request):
        animals_data = Main.objects.all()
        serializer = MainListSerializer(animals_data, many=True)
        return Response(serializer.data)

class Search(ListView):
    paginate_by = 10

    def get_queryset(self):
        return Main.objects.filter(nickname__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserCreationForm()
    return render(request, 'main_page/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'main_page/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('main')

def main(request):
    animals = Main.objects.all()
    return render(request, 'main_page/main_page.html', {'animals': animals})

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data')
    else:
        form = AddForm()
    return render(request, 'main_page/add.html', {'form': form})

def delete(request, id):
    nickname = Main.objects.get(id=id)
    nickname.delete()
    return redirect('main')

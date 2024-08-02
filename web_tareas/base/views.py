from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarea
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


class Logueo(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')


def register(request):
    """
    Fuction to register new users in the Users db model

    Args:
        request (HttpRequest object): HTTP request from client (browser)

    Returns:
        HttpResponse:
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Saving form user data in the model
            username = form.cleaned_data.get('username')
            message_to_show = f'User {username} created sucessfully!'
            messages.success(request, message_to_show.format(username))
    else:
        form = UserCreationForm()
    return render(request, 'base/registro.html', {'form': form})


def deslogueo(request):
    logout(request)
    return redirect('login')


# LoginRequiredMixin -> Deve ir priero de todos
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()
        valor_buscado = self.request.GET.get('area_buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        context ['valor_buscado'] = valor_buscado
        return context


class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')

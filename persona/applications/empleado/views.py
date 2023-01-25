from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from .models import Empleado
from .forms import EmpleadoForm
from .forms import LoginForm, PersonaForm

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

#Vistas para autenticacion
class LoginUser(FormView):
    template_name = 'empleado/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('persona_app:user-panel')
    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class Panel(LoginRequiredMixin, TemplateView):
    template_name = "empleado/panel.html"
    login_url = reverse_lazy('empleado_app:user-login')

class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'empleado_app:login-user'
            )
        )

class EmpleadoListView(LoginRequiredMixin,ListView):
    model = Empleado
    template_name = "empleado/listaLog.html"
    context_object_name = 'empleados'


class EmpleadoCreateView(LoginRequiredMixin,CreateView):
    model = Empleado
    template_name = "empleado/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:lista')


class Inicio(TemplateView):
    template_name = "inicio.html"

class EmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/lista.html"
    ordering = 'apellidos'
    context_object_name = 'empleados'


class BuscarEmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/buscar.html"
    ordering = 'apellidos'
    context_object_name = 'empleados'
    paginate_by = 3

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            apellidos__icontains = palabra_clave
        )
        return lista 


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detalle.html"
    context_object_name = 'detalle'



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/create.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:Lista de empleados')

    def form_valid(self, form):
        emp = form.save(commit=False)
        emp.nombre_completo = emp.nombres + '' + emp.apellidos 
        emp.save()
        return super(EmpleadoCreateView,self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/update.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:Lista de empleados')

    def form_valid(self, form):
        emp = form.save(commit=False)
        emp.nombre_completo = emp.nombres + '' + emp.apellidos 
        emp.save()
        return super(EmpleadoUpdateView,self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url = reverse_lazy('empleado_app:Lista de empleados')

        


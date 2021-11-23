from django.shortcuts import render
from .models import material
from .forms import CustomUserCreationForm , materialForm   
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def home(request):
    materiallistados = material.objects.all()
    return render(request,"gestion.html", {"cursos": materiallistados})

def top(request):
    materiales = material.objects.all()
    data = {
        "materiales": materiales
    }
    return render(request,"top.html", data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Exitoso")
            return redirect(to="/")
        data['form']=formulario
    
    return render(request, 'registration/registro.html', data)

def agregar_material(request):

    data= {
        'form': materialForm()

    } 

    if request.method == "POST":
        formulario = materialForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"]=formulario

    return render(request, "app/material/agregar.html", data)

def listar_material(request):
    material= material.objects.all()

    data = {
        'material': material 
    }

    return render(request, 'app/material/listar.html', data)

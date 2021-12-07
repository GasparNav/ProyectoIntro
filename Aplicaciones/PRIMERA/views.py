from django.shortcuts import render
from .models import material, comentario
from .forms import CustomUserCreationForm , materialForm, ComentariosForm
from django.shortcuts import redirect,get_object_or_404
from django.db.models import Q


# Create your views here.

def home(request):
    #matematicas:
    materiales = material.objects.order_by('-ratings__average')
    materiales_mate = materiales.filter(Q(etiquetas__icontains="matematicas")|Q(titulo__icontains="matematicas"))
    materiales_ciencias = materiales.filter(Q(etiquetas__icontains="ciencias")|Q(etiquetas__icontains="biologia")|Q(etiquetas__icontains="fisica")|Q(etiquetas__icontains="quimica"))
    materiales_lenguaje = materiales.filter(Q(etiquetas__icontains="lenguaje")|Q(titulo__icontains="lenguaje"))
    materiales_historia = materiales.filter(Q(etiquetas__icontains="historia")|Q(titulo__icontains="historia"))

    data = {
        'materiales_historia': materiales_historia,
        'materiales_mate': materiales_mate,
        'materiales_ciencias': materiales_ciencias,
        'materiales_lenguaje': materiales_lenguaje,

    }
    return render(request, 'gestion.html', data)

    

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


def detalle(request):
    id = request.GET.get('id', '')
    materiales = material.objects.filter(id=id)
    comentarios = comentario.objects.filter(material_id=id)
    data = {
        "materiales": materiales,
        "comentarios": comentarios
        }
    return render(request,"detalle.html", data)

def search(request):
    materiales = material.objects.order_by('fecha_subida')
    #materiales  = ''
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            materiales = materiales.filter(Q(etiquetas__icontains=keyword)|Q(descripcion__icontains=keyword)|Q(titulo__icontains=keyword))

    data = {
        'materiales': materiales,
    }
    return render(request, 'buscar.html', data)

def agregar_comentario(request):
    id = request.GET.get('id', '')
    material_s = get_object_or_404(material, id=id)

    if request.method == "POST":
        form = ComentariosForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.material = material_s
            comment.save()
            #messages.success(request, "Registro Exitoso")
            return redirect(to="/")
            #return redirect('/detalle', id=id)
    else:
        form = ComentariosForm()
        return render(request, 'comentarios.html', {'form': form})

def qs(request):
    return render(request,"quienessomos.html")
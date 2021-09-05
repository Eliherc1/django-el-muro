from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required,admin_requerido
from .models import *

@login_required
def index(request):

    context = {
        'mensajes': Message.objects.all() ,
        'comentarios': Comment.objects.all()

    }
    return render(request, 'index.html', context)



@admin_requerido
def administrador(request):

    context = {
        'saludo': 'ADMINISTRADOR'
    }
    return render(request, 'admin.html', context)


def procesar_mensaje(request):
    print(request.POST)

    mensaje = Message.objects.create(
        message = request.POST['men'],
        user_m = User.objects.get(id=request.session['usuario']['id'])
        
    )

    return redirect("/")


def procesar_comentario(request):
    print(request.POST)

    comentario = Comment.objects.create(
        comment = request.POST['comment'],
        user_c = User.objects.get(id=request.session['usuario']['id']) ,
        message = Message.objects.get(id=request.POST['men_id'])
        
    )

    return redirect("/")

def eliminar_comentario(request, id):
    c = Comment.objects.get(id=id)
    c.delete()
    return redirect("/")

def eliminar_mensaje(request, id):
    m = Message.objects.get(id=id)
    m.delete()
    return redirect("/")

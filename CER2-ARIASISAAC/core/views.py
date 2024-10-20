from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import re
from core.models import Pedido, Producto
from django.contrib.auth.models import User  

from core.carrito import Carrito 
# Create your views here.
def home(request):
    return render(request, "core/index.html")

def catalogo(request):
    productos = Producto.objects.all()
    return render(request,"core/catalogo.html",{"productos": productos})


def agregar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.add(producto)
    return redirect("carrito")

def eleminar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eleminar(producto)
    return redirect("carrito")

def eliminar_grupo_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar_grupo(producto)
    return redirect("carrito")

def restar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def solicitud(request):
    return render(request,"core/solicitud.html")

def signup(request):
    data = {
        'form':UserCreationForm
    }

    email = request.POST.get('email', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    username = request.POST.get('username', '')
    flag = True

   
    
    if(request.method == 'GET'):
        return render(request, 'registration/signup.html',data)
    else:
        #################### VALIDACIONES ##########################
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if( not re.match(email_regex,email ) or 
            len(email) == 0 or 
            (len(password2) == 0 and 
            len(password1) == 0) or  
            len(username) == 0):
            flag = False
        ############################################################
        print(request.POST)
        if(flag):
            if(request.POST['password1'] == request.POST['password2'] ):
                try:
                    user = User.objects.create_user(email=request.POST['email'], username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect("home")
                    
                except:
                    data = {
                        'form':UserCreationForm,
                        'error1': 'Nombre de usuario ya existe, intenta otro'
                    }
                    return render(request, 'registration/signup.html', data)
            data = {
                'form':UserCreationForm,
                'error2': 'Las contraseñas no coinciden'
            }
            return  render(request, 'registration/signup.html', data)
        else:
            data = {
                'form':UserCreationForm,
                'error3': 'Llene todos los campos requeridos'
            }
            return  render(request, 'registration/signup.html', data)
    
def protected(request):
    return render(request, "core/protected.html")    

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    data = {
        'form':UserCreationForm
    }
    username = request.POST.get('username', '')
    password1 = request.POST.get('password1', '')
    flag = True

    
    if(request.method == 'GET'):
        return render(request, 'registration/signin.html',data)
    else:
        #################### VALIDACIONES ##########################
        if(len(username) == 0 or len(password1) == 0):
            flag = False
        ############################################################
        print(flag)
        if(flag):
                
            print(request.POST)
            user = authenticate(request, username= request.POST['username'], password=request.POST['password1'])
        
            if user is None:
                data = {
                    'form':UserCreationForm,
                    'error1': ' usuario o contraseña incorrectas'
                }
            else:
                login(request, user)
                return redirect(home)
        else:
            data = {
                'form':UserCreationForm,
                'error2':' debe ingresar informacion en ambos campos'
            }
    return render(request, 'registration/signin.html', data) 

def carrito(request):
    return render (request,"core/carrito.html")


def envio_pedido(request):
    if request.method == 'POST':
        # Obtener los datos del carrito de la sesión
        carrito = request.session.get('carrito', {})
        correo_usuario = request.user.email # Obtener el usuario logueado
        
        # Recorrer los productos en el carrito y guardar cada uno como un Pedido
        for key, value in carrito.items():
            nombre_producto = value['nombre']
            cantidad = value['cantidad']
            precio_parcial = value['acumulado']

            # Crear una instancia del modelo Pedido y guardar en la base de datos
            pedido = Pedido(
                nombre = nombre_producto,
                cantidad=cantidad,
                precio_parcial = precio_parcial,
                estado = "Pendiente",
                correo = correo_usuario)
            
            pedido.save()

        # Redirigir o mostrar mensaje de éxito
        return redirect('carrito')  # Puedes cambiar esta vista según lo que necesites
    else:
    
        return redirect('core/carrito')
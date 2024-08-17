from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Imagen
from .forms import PostForm, FiltroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from accounts.forms import RegistroForm, PerfilForm 
from accounts.models import Perfil  # Suponiendo que el modelo Perfil está en accounts/models.py

def listar_posts(request):
    form = FiltroForm(request.GET)
    posts = Post.objects.all().prefetch_related('imagenes')

    if form.is_valid():
        categoria = form.cleaned_data['categoria']
        color = form.cleaned_data['color']
        zona = form.cleaned_data['zona']

        if categoria and categoria != '----':
            posts = posts.filter(categoria=categoria)
        if color and color != '----':
            posts = posts.filter(color=color)
        if zona and zona != '----':
            posts = posts.filter(zona__icontains=zona)

    return render(request, 'blog/lista_posts.html', {'posts': posts, 'form': form})


def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    imagenes = post.imagenes.all()
    autor_perfil = get_object_or_404(Perfil, user=post.autor)
    
    return render(request, 'blog/detalle_post.html', {
        'post': post,
        'imagenes': imagenes,
        'autor_perfil': autor_perfil
    })

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()

            for img in request.FILES.getlist('imagenes'):
                Imagen.objects.create(post=post, imagen=img)
            return redirect('listar_posts')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def perfil(request):
    print("Entrando a la vista del perfil")
    # Obtener o crear el perfil del usuario
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    
    # Manejar la actualización del perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige al perfil después de guardar
    else:
        form = PerfilForm(instance=perfil, user=request.user)
    
    # Filtrar publicaciones del usuario que ha iniciado sesión
    user_posts = Post.objects.filter(autor=request.user)

    return render(request, 'accounts/perfil.html', {
        'form': form,
        'user_posts': user_posts,
    })


@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Verificación de permisos
    if not (request.user.is_superuser or request.user == post.autor):
        return redirect('listar_posts')  # O cualquier otra página de error

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            post_modificado = form.save(commit=False)
            
            # Manejo de imágenes
            if 'imagenes' in request.FILES:
                post.imagenes.all().delete()  # Eliminamos las imágenes anteriores
                for img in request.FILES.getlist('imagenes'):
                    Imagen.objects.create(post=post, imagen=img)
            
            post_modificado.save()
            return redirect('profile')
    else:
        form = PostForm(instance=post)
    
    imagenes = post.imagenes.all()
    return render(request, 'blog/editar_post.html', {'form': form, 'imagenes': imagenes})


@login_required
def borrar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if not (request.user.is_superuser or request.user == post.autor):
        return redirect('listar_posts')  # O cualquier otra página de error

    if request.method == 'POST':
        post.delete()
        return redirect('profile')
    return render(request, 'blog/borrar_post.html', {'post': post})


def acerca_de_mi(request):
    return render(request, 'blog/acercademi.html')
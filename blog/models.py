from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORIA_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]

    COLOR_CHOICES = [
        ('Negro', 'Negro'),
        ('Blanco', 'Blanco'),
        ('Marrón', 'Marrón'),
        ('Gris', 'Gris'),
        # Añade otros colores según sea necesario
    ]
    ZONA_CHOICES = [
        ('Sur', 'Sur'),
        ('Centro', 'Centro'),
        ('Norte', 'Norte'),
        ('Este', 'Este'),
        ('Oeste', 'Oeste'),
    ]

    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=5, choices=CATEGORIA_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    zona = models.CharField(max_length=100, choices=ZONA_CHOICES)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


class Imagen(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f"Imagen de {self.post.titulo}"
import uuid  # Importamos la biblioteca uuid para generar códigos únicos
from django.db import models

# Create your models here.

class Noticia(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)  
    titulo = models.CharField(max_length=200)
    reportero = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
    
     # Sobrescribimos el método save() que se llama cuando se guarda una instancia del modelo
    def save(self, *args, **kwargs):
        # Si el campo 'codigo' está vacío, generamos un código único
        if not self.codigo:
            self.codigo = self.generate_unique_code()
        # Llamamos al método save() de la clase padre para guardar la instancia en la base de datos
        super().save(*args, **kwargs)

    # Definimos un método para generar un código único
    def generate_unique_code(self):
        # Generamos un UUID, lo convertimos a cadena y tomamos los primeros 10 caracteres
        return str(uuid.uuid4())[:10]
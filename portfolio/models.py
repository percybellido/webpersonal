from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=100, verbose_name="Titulo")
    description=RichTextField(verbose_name="Descripción")
    image=models.ImageField(verbose_name="Imagen", upload_to="projects")
    link=models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        ordering=["-created"]
    
    def __str__(self):
        return self.title
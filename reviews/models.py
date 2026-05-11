from django.db import models

# Create your models here.
class Review(models.Model):
    nombre=models.CharField(max_length=100)
    comentario=models.TextField(max_length=200)
    estrellas=models.IntegerField()
    imagen=models.ImageField(
        upload_to='reviews',
        null=True,
        blank=True
    )
    fecha=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-fecha']

    def __str__(self):
        return f"{self.nombre} - {self.estrellas} estrellas"
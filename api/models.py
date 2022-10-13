from django.db import models

NACIONALIDAD = (('Mexicana', 'Mexicana'), ('Inglesa', 'Inglesa'), ('Española', 'Española'))


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(verbose_name="Autor", max_length=100)
    nacionalidad = models.CharField(choices=NACIONALIDAD, verbose_name="Nacionalidad", max_length=30, default="Mexicana")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Libro(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    Autor = models.ForeignKey(Autor, verbose_name="Seleccione autor", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

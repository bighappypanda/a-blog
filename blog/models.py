from django.db import models # ONLY PRESET LINE
from django.utils import timezone

# Create your models here.
# Model: POST (object)

class Post(models.Model): #models.Model indica que Post es un modelo Django 
    # que debe guardarse en la base de datos
   # PROPIEDADES O ATRIBUTOS
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #Vínculo con otro modelo
    title = models.CharField(max_length=200) # Texto con # limitado caracteres
    text = models.TextField() # Texto sin limite
    created_date = models.DateTimeField(default=timezone.now) #Fecha y hora
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

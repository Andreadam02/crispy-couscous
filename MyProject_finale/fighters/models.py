from django.db import models

# Create your models here.
class Fighter(models.Model):
    immagine = models.ImageField(upload_to='uploaded_fighters/', max_length=100)
    nome = models.CharField(max_length=20)
    descrizione = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    upload_date = models.DateTimeField(auto_now_add=True)

def upload_to(instance, filename):
    return 'uploaded_files/{0}'.format(filename)

    def __str__(self):
        return self.file.name
    




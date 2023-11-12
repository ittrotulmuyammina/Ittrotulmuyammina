from django.db import models

# Create your models here.

class Macam_Book(models.Model):
    Macam_Book = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Macam_Book}"

class Book(models.Model):
    Macam_Book = models.ForeignKey(Macam_Book, on_delete=models.CASCADE)
    Judul = models.CharField(max_length=100)
    Tahun_Penerbit = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Judul} {self.Tahun_Penerbit}"
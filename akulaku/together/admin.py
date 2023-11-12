from django.contrib import admin
from .models import Book, Macam_Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display =("Judul","Tahun_Penerbit",)

admin.site.register(Book,BookAdmin)
admin.site.register(Macam_Book)
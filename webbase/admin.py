from django.contrib import admin
from .models import Producto



class ProductoAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.nombre

admin.site.register(Producto,ProductoAdmin)
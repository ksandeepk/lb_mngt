from django.contrib import admin
from .models import book
# Register your models here.
class bookAdmin(admin.ModelAdmin):
    list_display = ('book_id','book_name','author','Image','Documents','branch')


admin.site.register(book,bookAdmin)

from django.contrib import admin
from .models import Poems, PoemsAuthor, Poetry, PoetryAuthor
# Register your models here.
admin.site.register(Poems)
admin.site.register(PoemsAuthor)
admin.site.register(Poetry)
admin.site.register(PoetryAuthor)

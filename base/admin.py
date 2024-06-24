from django.contrib import admin

# Register your models here.
from .models import Employe, Entreprise, AdministrateurPlanning, Poste, TeamPlanning, CustomUser

admin.site.register(Employe)
admin.site.register(Entreprise)
admin.site.register(AdministrateurPlanning)
admin.site.register(Poste)
admin.site.register(TeamPlanning)
admin.site.register(CustomUser)
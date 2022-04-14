from django.contrib import admin

from cmmapp.models import allergie, categorie, contreIndication, patient, rdv, triage, utilisateur

# Register your models here.
admin.site.register(patient)
admin.site.register(utilisateur)
admin.site.register(categorie)
admin.site.register(allergie)
admin.site.register(contreIndication)
admin.site.register(triage)
admin.site.register(rdv)



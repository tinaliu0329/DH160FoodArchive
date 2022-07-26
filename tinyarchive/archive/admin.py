from django.contrib import admin
from archive.models import Photograph,Document,Artifact
# Register your models here.

admin.site.register(Photograph)
admin.site.register(Document)
admin.site.register(Artifact)
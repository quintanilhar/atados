from django.contrib import admin
from atados.project import models


admin.site.register(models.Apply)
admin.site.register(models.Availability)
admin.site.register(models.Cause)
admin.site.register(models.Skill)
admin.site.register(models.Project)
admin.site.register(models.ProjectWork)
admin.site.register(models.ProjectDonation)

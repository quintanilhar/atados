from django.contrib import admin
from atados.project.models import (Classification, Project,
                                   ProjectWork, ProjectDonation)


admin.site.register(Classification)
admin.site.register(Project)
admin.site.register(ProjectWork)
admin.site.register(ProjectDonation)

from django.contrib import admin
from atados.project import models


class ProjectAdmin(admin.ModelAdmin):
    list_filter = ('published',)
    exclude = ('deleted', 'deleted_date',)

    def queryset(self, request):
        qs = self.model._default_manager.active()
        ordering = self.ordering or () 
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

admin.site.register(models.Apply)
admin.site.register(models.Availability)
admin.site.register(models.Cause)
admin.site.register(models.Skill)
admin.site.register(models.ProjectJob, ProjectAdmin)
admin.site.register(models.ProjectWork, ProjectAdmin)
admin.site.register(models.ProjectDonation, ProjectAdmin)

from django.contrib import admin

from netcovapp.models import Coverage, City, Operator


class CoverageAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class OperatorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coverage, CoverageAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Operator, OperatorAdmin)

from django.contrib import admin
from .models import (
    GlassCategory,
    Glass,
    GlassBrand,
    Watch,
    WatchCategory,
    WatchBrand,
    Coffe,
    CoffeCategory,
    CoffeBrand,
)

# class HeroSectionAdmin(admin.ModelAdmin):
#     list_display = ("title",)

#     list_filter = ("title",)
#     search_fields = (
#         "title",
#         "description",
#     )


admin.site.register(Glass)
admin.site.register(GlassCategory)
admin.site.register(GlassBrand)

admin.site.register(Watch)
admin.site.register(WatchCategory)
admin.site.register(WatchBrand)


admin.site.register(Coffe)
admin.site.register(CoffeCategory)
admin.site.register(CoffeBrand)

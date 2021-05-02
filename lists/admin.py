from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin Definition """

    list_display = ("name", "user", "count_rooms")

    search_fields = ("name",)  # name으로만 검색가능

    filter_horizontal = ("rooms",)

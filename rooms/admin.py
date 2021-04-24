from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    # 어드민패널에서 field를 보여주는 방식을 정해줌
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "price", "address")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Space",
            {  # 접을 수 있는 섹션을 만들어줌
                "classes": ("collapse",),
                "fields": ("room_type", "amenities", "facilities", "house_rules"),
            },
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("Last Details", {"fields": ("host",)}),
    )

    # 목록 미리보기
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    # 정렬 기준
    ordering = ("name", "price")

    # 필터
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    # 검색대상, User와 ForeignKey로 연결된 host로 username불러오기.
    search_fields = ("city", "^host__username")

    # many to many 관계를 가진 변수를 awesome하게 만들어 줌
    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()
        # room에서 amenities에 접근해 데이터들의 갯수를 리턴함(many to many로 연결되어 있기 때문에 가능)

    def count_photos(self, obj):
        return obj.photos.count()
        # room에서 photos에 접근해 데이터들의 갯수를 리턴함(related_name="photos"로 연결되있기 때문에 가능, photos_set이 원래 명령어)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass

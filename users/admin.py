from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # UserAdmin을 사용하고 싶음.
from . import models  # .은 동일한 폴더내에서 찾는다는 의미

# Register your models here.
# admin 패널에서 이 user를 보고싶음. user를 컨트롤한 클래스가 아래의 것이다. @ : 데코레이터
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # 장고에서 기본 제공하는 fieldsets과 내가 만든 fieldsets을 삽입. fieldset : field공간.
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

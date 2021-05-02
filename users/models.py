from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractUser로 user만들기위해서 import

# AbstractUser를 객체상속받아서 사용.
class User(AbstractUser):

    """ Custom User Model """  # it is docstring

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),  # (데이터베이스로 갈 데이터, Form에서 보여질 데이터)
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))
    # field : html에서의 form으로 이해
    avatar = models.ImageField(
        upload_to="avatars", blank=True
    )  # 이미지form. pillow패키지 설치 해야 됨. form에서 blank허용.uploads/avatars폴더에 이미지가 업로드 됨
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True
    )  # 단어텍스트form. choices로 커스터마이징.
    bio = models.TextField(blank=True)  # 문장텍스트form. 데이터베이스에 default값으로 ""
    birthdate = models.DateField(blank=True, null=True)  # 데이터베이스에 null허용.
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)  # boolean 참거짓  field. 체크박스form으로 나옴

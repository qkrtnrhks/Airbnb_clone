from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)  # 아이템들 이름 적는곳

    class Meta:
        abstract = True  # 어드민 패널에서 숨기기, 이 모델은 데이터베이스에 저장x, 반복되는 코드를 막고 빠른실행을 위해

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"  # Meta 클래스로 이 model이 admin패널에서 보여지는 이름 바꾸기


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(
        "Room", related_name="photos", on_delete=models.CASCADE
    )  # string타입이면 import안하고도 찾기가능


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE
    )  # user와 room model을 일대다로 연결. 다른 app속의 model도 가져올 수 있음. string타입이 아닐땐 import후 사용. CASCADE : 삭제되면 연관된것들도 삭제됨
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField(
        Amenity, related_name="rooms", blank=True
    )  # Amenity와 room model을 다대다로 연결. related_name :연결된 각각의 모델들을 식별하기 위해사용, 모델이름__set을 다른 이름의 명령어로 변경
    # _set :지목당한 모델이 지목한 모델에 대한 정보를 얻을 수 있게함.(amenities를 통해 rooms의 정보를 가져옴 : amenities.rooms_set.all())
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name  # object를 string으로 바꿔줌. (room이름으로)

    def total_rating(self):
        all_reviews = self.review.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        if len(all_reviews) > 0:
            return round(all_ratings / len(all_reviews), 2)
        else:
            return 0

from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (
            STATUS_CANCELED,
            "Canceled",
        ),
    )

    status = models.CharField(
        max_length=13, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservation", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservation", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"  # 파이썬이므로 format 사용가능

    def in_progress(self):  # 메소드만들기
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True  # true false를 o x 기호로 바꿔줌

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

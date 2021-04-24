from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateField(auto_now_add=True)  # model이 생성된 날짜
    updated = models.DateField(auto_now=True)  # 새로운 날짜를 업데이트

    # 데이터베이스에 저장되지 않게 하기위해. abstract
    # 어드민 패널에서 숨기기, 이 모델은 데이터베이스에 저장x, 반복되는 코드를 막고 빠른실행을 위해
    class Meta:
        abstract = True
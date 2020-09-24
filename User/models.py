from django.db import models


# Create your models here.
class User(models.Model):
    genders = (
        ('male', '男'),
        ('female', '女')
    )
    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('成都', '成都'),
        ('西安', '西安'),
        ("武汉", "武汉"),
        ("沈阳", "沈阳")
    )
    phonenum = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    nickename = models.CharField(verbose_name='昵称', max_length=20, db_index=True)
    gender = models.CharField(verbose_name='性别',max_length=10, choices=genders, null=True)
    birthday = models.DateField(verbose_name='出生日期', default='2000-06-06')
    avatar = models.CharField(verbose_name='个人形象', max_length=256)
    location = models.CharField(verbose_name='居住地', choices=LOCATIONS, max_length=10)

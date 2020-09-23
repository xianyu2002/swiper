from django.db import models

# Create your models here.
class User(models.Model):
    phonenum=models.CharField(name='手机号',max_length=11,default=1,null=False)
    nickename=models.CharField(name='昵称',max_length=32,default='')
    gender=models.NullBooleanField(name='性别',default=0,null=True)
    birthday=models.DateField(name='出生日期',default='2000-06-06')
    avatar=models.ImageField(name='个人形象',default='')
    location=models.CharField(name='居住地',max_length=64,default='北京')


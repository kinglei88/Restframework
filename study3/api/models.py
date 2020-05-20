from django.db import models

# Create your models here.


class UserGroup(models.Model):
    title = models.CharField(max_length=32)



class UserInfo(models.Model):
    user_type_choice = (
        (1,'普通用户'),
        (2,'VIP'),
        (3,'SVIP'),
    )

    user_type = models.IntegerField(choices=user_type_choice)
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)

    group = models.ForeignKey('UserGroup')
    role = models.ManyToManyField('Role')

    class Meta():
        db_table = 'userinfo'



class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo')
    token = models.CharField(max_length=64)




class Role(models.Model):
    title = models.CharField(max_length=32)
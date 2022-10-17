from django.db import models


# Create your models here.
class Human(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=50)
    is_married = models.BooleanField()
    role = models.ForeignKey('Role', on_delete=models.PROTECT)
    password = models.CharField(max_length=100, default='')
    email = models.EmailField(default='cawa@cawa.cawa')

    def __str__(self):
        return "Human characteristic for {}".format(self.first_name)


class Deleted(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=50)
    is_married = models.BooleanField()
    role = models.ForeignKey('Role', on_delete=models.PROTECT)
    password = models.CharField(max_length=100, default='')
    email = models.EmailField()
    time_deleted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Human characteristic for {}".format(self.first_name)


class Role(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name

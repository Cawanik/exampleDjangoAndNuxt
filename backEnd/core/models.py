from django.db import models


# Create your models here.
class Human(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=50)
    is_married = models.BooleanField()
    role_id = models.ForeignKey('Role', on_delete=models.PROTECT)

    def __str__(self):
        return "Human characteristic for {}".format(self.first_name)


class Role(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

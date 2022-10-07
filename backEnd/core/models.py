from django.db import models


# Create your models here.
class Human(models.Model):
    MARRIED = (
        ('Y', 'Is married'),
        ('N', 'Is not married'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=50)
    is_married = models.BooleanField()
    role_id = models.PositiveIntegerField()

    def __str_(self):
        return "Human characteristic for {}".format(self.first_name)

from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100, null=False)
    email=models.EmailField(null=False,max_length=100)
    mobile=models.IntegerField(null=False)

    def __str__(self):
        return self.name
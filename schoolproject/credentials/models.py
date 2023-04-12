from django.db import models
#
# # Create your models here.
# class Department(models.Model):
#     name=models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name
# class Course(models.Model):
#     country=models.ForeignKey(Department,on_delete=models.CASCADE)
#     name=models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name
# class Person(models.Model):
#     name=models.CharField(max_length=124)
#     department=models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
#     course=models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)
#
#     def __str__(self):
#         return self.name
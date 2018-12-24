from django.db import models
from django.core.exceptions import ValidationError


LONG_CHAR = 512
SHORT_CHAR = 32


def validate_num(num):
    if num < 0:
        raise ValidationError("请输入正数！")


class School(models.Model):
    objects = models.Manager()
    school_id = models.AutoField(primary_key=True, verbose_name='', db_index=True)
    area_code = models.CharField(max_length=SHORT_CHAR, )


class Class(models.Model):
    objects = models.Manager()


class Student(models.Model):
    objects = models.Manager()


class Teacher(models.Model):
    objects = models.Manager()


class Assignment(models.Model):
    objects = models.Manager()


class Exam(models.Model):
    objects = models.Manager()


class Problem(models.Model):
    objects = models.Manager()


class AssignmentCondition(models.Model):
    objects = models.Manager()


class Tab(models.Model):
    objects = models.Manager()




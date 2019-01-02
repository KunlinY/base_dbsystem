# -*- coding: UTF-8 -*-

from mongoengine import fields
from mongoengine import *
# admin里面看不见的话把这行去掉 上行注释
# from django_mongoengine import *


class Subject(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()


class Book(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    series = fields.StringField()
    subject = fields.ReferenceField(Subject)


class Chapter(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    book = fields.ReferenceField(Book)
    sub = fields.ListField(fields.ReferenceField('Chapter'))


class School(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    area_code = fields.StringField()
    administrator = fields.StringField()
    types = fields.StringField()
    rank = fields.IntField()
    description = fields.StringField()
    register = fields.StringField()


class Group(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    rank = fields.IntField()
    year = fields.DateField()
    school = fields.ReferenceField(School)


class Folder(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    sub = fields.ListField(fields.ReferenceField('Folder'))
    problems = fields.ListField(fields.ReferenceField('Problem'))
    exercises = fields.ListField(fields.ReferenceField('Exercise'))


class People(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    born = fields.DateField()
    sexuality = fields.StringField()
    school = fields.ReferenceField(School)
    group = fields.ListField(fields.ReferenceField(Group))
    year = fields.DateField()
    types = fields.StringField()
    email = fields.EmailField()
    password = fields.StringField()
    favorites = fields.ReferenceField(Folder)

    meta = {'allow_inheritance': True}


class Teacher(People):
    position = fields.StringField()
    subject = fields.ListField(fields.ReferenceField(Subject))


class Student(People):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    effort = fields.IntField()
    frustration = fields.IntField()
    habits = fields.IntField()
    correction = fields.IntField()
    comprehension = fields.IntField()
    logics = fields.IntField()
    abstraction = fields.IntField()
    imagination = fields.IntField()
    summary = fields.IntField()


class Solution(Document):
    _id = fields.ObjectIdField()
    description = fields.ListField(fields.StringField())
    images = fields.ListField(fields.ImageField())
    formula = fields.ListField(fields.StringField())


class Problem(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    types = fields.StringField()
    description = fields.ListField(fields.StringField())
    images = fields.ListField(fields.ImageField())
    formula = fields.ListField(fields.StringField())
    sub = fields.ListField(fields.ReferenceField('Problem'))
    book = fields.ReferenceField('Book')
    chapter = fields.ReferenceField('Chapter')
    tags = fields.ListField(fields.ReferenceField('Tag'))
    solutions = fields.ListField(fields.ReferenceField('Solution'))


class Exercise(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    types = fields.StringField()
    problems = fields.ListField(fields.ReferenceField(Problem))
    final_results = fields.ListField(fields.IntField())
    allow_time = fields.IntField()
    publish_time = fields.DateTimeField()
    aim = fields.StringField()
    publisher = fields.ListField(fields.ReferenceField(People))
    targets = fields.ListField(fields.ReferenceField(Student))
    subject = fields.ReferenceField(Subject)


class Tag(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    description = fields.StringField()
    types = fields.StringField()
    difficulty = fields.IntField()
    book = fields.ReferenceField(Book)
    topic = fields.ListField(fields.ListField(fields.ReferenceField(Chapter)))


class Wrong(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    description = fields.StringField()
    tags = fields.ListField(fields.ReferenceField(Tag))


class ProblemCondition(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    student = fields.ReferenceField(Student)
    problem = fields.ReferenceField(Problem)
    result = fields.StringField()
    wrong = fields.ListField(fields.StringField())
    times = fields.IntField()


class ExerciseCondition(Document):
    _id = fields.ObjectIdField()
    name = fields.StringField()
    student = fields.ReferenceField(Student)
    degree = fields.IntField()
    result = fields.StringField()
    times = fields.IntField()

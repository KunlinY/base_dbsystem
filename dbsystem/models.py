# -*- coding: UTF-8 -*-

from django.db import models
from django.core.exceptions import ValidationError


LONG_CHAR = 512
SHORT_CHAR = 64
CODE_CHAR = 16


class Subject(models.Model):
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='科目ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='科目名字')

    class Meta:
        verbose_name = '科目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Tag(models.Model):
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='标签ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='标签名字')
    category = models.CharField(max_length=CODE_CHAR, verbose_name='标签类型', choice=(('T', '题型'), ('N', '能力'), ('Z', '知识'), ('C', '易错')))
    difficulty = models.IntegerField(verbose_name='标签难度')
    description = models.CharField(max_length=LONG_CHAR, verbose_name='标签描述')
    book = models.ForeignKey(Book, verbose_name='书目')
    chapter = models.ForeignKey(Chapter, verbose_name='章节')
    precursor = models.ManyToManyField("Tag", verbose_name='前序知识')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    

class TagAbility(models.Model):
    objects = models.Manager()
    student = models.ForeignKey(Student, verbose_name='学生')
    tag = models.ForeignKey(Tag, verbose_name='标签')
    degree = models.IntegerField(verbose_name='掌握程度')

    class Meta:
        verbose_name = '学生标签掌握程度'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student.name + '@' + self.tag.name

    def __repr__(self):
        return self.student.name + '@' + self.tag.name


class School(models.Model):
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='学校ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='学校名字')
    area = models.CharField(max_length=CODE_CHAR, verbose_name='所属地区代码')
    administrator = models.CharField(max_length=SHORT_CHAR, verbose_name='所属单位')
    property = models.CharField(max_length=CODE_CHAR, verbose_name='学校性质', choices=(('public', ''), ('private', ''), ('other', '')))
    rank = models.IntegerField(verbose_name='学校区县排名')
    description = models.CharField(max_length=LONG_CHAR, verbose_name='学校描述')
    level = models.CharField(max_length=CODE_CHAR, verbose_name='学校等级', choices=(('provincial', ''), ('municipal', ''), ('county', ''), ('other', '')))

    class Meta:
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Class(models.Model):
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='班级ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='班级名字')
    entry_year = models.IntegerField(verbose_name='入学年份')
    rank = models.IntegerField(verbose_name='班级排名')

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class People(models.Model):
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='人员ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='人员名字')
    entry_year = models.IntegerField(verbose_name='入职年份')
    born_year = models.IntegerField(verbose_name='出生年份')
    sex = models.CharField(max_length=CODE_CHAR, verbose_name='性别',
                           choices=(('male', '男'), ('female', '女'), ('other', '未知')))
    school = models.ForeignKey(School, verbose_name='所属学校')
    classes = models.ManyToManyField(Class, verbose_name='所属班级')

    class Meta:
        verbose_name = '人员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Teacher(People):
    position = models.CharField(max_length=SHORT_CHAR, verbose_name='老师职位')
    subject = models.ForeignKey(Subject, verbose_name='教授学科')

    class Meta:
        verbose_name = '老师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Student(People):
    subjects = models.ManyToManyField(Subject, verbose_name='考试学科')
    hardness = models.IntegerField(verbose_name='努力程度')
    frustration = models.IntegerField(verbose_name='抗挫折能力')
    habit = models.IntegerField(verbose_name='学习习惯')
    correct = models.IntegerField(verbose_name='改正能力')
    comprehensive = models.IntegerField(verbose_name='理解力')
    logic = models.IntegerField(verbose_name='逻辑思维能力')
    abstract = models.IntegerField(verbose_name='抽象思维能力')
    spatial = models.IntegerField(verbose_name='空间想象力')
    conclusive = models.IntegerField(verbose_name='归纳总结能力')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Problem(models.Model):
    #（题目ID，出题人，出题对象，出题目的（思考/新接触/巩固/评测），录入者ID，平均准确率，平均做题用时，
    # 做题总次数，总标记次数，总回看次数，经典错误答案，错误答案类别列表，答案，详细解答，步骤(每一步的具体内容)
    # ，步骤标签列表（只有有步骤的时候才启用），标签列表，题目类别（判断/选择/填空/解答/证明），属于的书目，
    # 属于的章节，属于的小节，属于页码）
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='问题ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='问题名字')
    point = models.IntegerField(verbose_name='分值')


class Exercise(models.Model):
    # 关于每次不同分值的问题，还是应该把题目和考试的关系单独拉出来
    # 题目和考试的关系，不仅有分值还有序数关系，第1题和第20题
    # 在考试中不一样，在这点上作业也一样
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='作业ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='练习名字')
    problems = models.ManyToManyField(Problem, verbose_name='题目列表')
    release_time = models.DateTimeField(verbose_name='布置时刻')
    length = models.IntegerField(verbose_name='布置时长')
    aim = models.CharField(max_length=CODE_CHAR, verbose_name='布置目的',
                           choices=(('1', '思考'), ('2', '新接触'), ('3', '巩固'), ('4', '评测')))
    release_people = models.ForeignKey(Teacher, verbose_name='布置人')
    release_target = models.ManyToManyField(Teacher, verbose_name='布置对象')
    subject = models.ForeignKey(Subject, verbose_name='学科')
    types = models.CharField(max_length=CODE_CHAR, verbose_name='练习类型',
                             choices=(('1', '作业'), ('2', '考试'), ('3', '其他')))

    class Meta:
        verbose_name = '练习'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.entity_id

    def __repr__(self):
        return self.entity_id


class ProblemCondition(models.Model):
    objects = models.Manager()
    student = models.ForeignKey(Student, verbose_name='学生')
    problem = models.ForeignKey(Problem, verbose_name='问题')
    result = models.CharField(max_length=LONG_CHAR, verbose_name='题目完成结果')
    # 题目完成情况应该是多次练习的一个汇总（一个学生可能反复做一道题）
    # 所以需要加入回看（回看应该要记录回看的时刻）、和特殊标记（这个特殊标记由学生自己打）
    # 所以可能需要加入回看和特殊标记类
    #condition应该不需要错误答案列表
    judge = models.CharField(max_length=LONG_CHAR, verbose_name='错误答案列表')
    cost = models.IntegerField(verbose_name='完成所花时间')

    class Meta:
        verbose_name = '题目完成情况'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student.name + '@%d' % self.problem.entity_id

    def __repr__(self):
        return self.student.name + '@%d' % self.problem.entity_id


class ExerciseCondition(models.Model):
    objects = models.Manager()
    # 如果是考试还需要要每道题的得分
    exercise = models.ForeignKey(Exercise, verbose_name='练习')
    student = models.ForeignKey(Student, verbose_name='学生')
    finish_time = models.DateTimeField(verbose_name='完成时间')
    finish_degree = models.IntegerField(verbose_name='完成程度')
    # result应该指向正确、错误或者经典错误答案
    results = models.ManyToManyField(ProblemCondition, verbose_name='题目完成结果列表')

    class Meta:
        verbose_name = '练习完成情况'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student.name + '@%d' % self.exercise.entity_id

    def __repr__(self):
        return self.student.name + '@%d' % self.exercise.entity_id


class Book(models.Model):
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='书目ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='书目名称')
    series = models.CharField(max_length=SHORT_CHAR, verbose_name='书目系列')
    subject = models.ForeignKey(Subject, verbose_name='科目')


    class Meta:
        verbose_name = '书目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + "@" + self.series

    def __repr__(self):
        return self.name + "@" + self.series

class Chapter(models.Model):
    objects = models.Manager()
    entity_id = models.AutoField(primary_key=True, verbose_name='章节ID', db_index=True)
    name = models.CharField(max_length=SHORT_CHAR, verbose_name='章节名称')
    book = models.ForeignKey(Book, verbose_name='书目')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + "@" + self.book.name + "@" + self.book.series

    def __repr__(self):
        return self.name + "@" + self.book.name + "@" + self.book.series

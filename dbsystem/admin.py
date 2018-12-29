from django.contrib import admin
from .models_mysql import *

admin.site.register(Subject)
admin.site.register(Tag)
admin.site.register(TagAbility)
admin.site.register(School)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Problem)
admin.site.register(Exercise)
admin.site.register(ProblemCondition)
admin.site.register(ExerciseCondition)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Stuff)


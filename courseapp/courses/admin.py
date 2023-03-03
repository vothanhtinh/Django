from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django import forms
from ckeditor_uploader.widgets \
import CKEditorUploadingWidget


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(forms.ModelForm):
    content= forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    list_display = ['id','subject','create_day','updated_day']
    list_filter = ['id','subject','create_day','updated_day']
    search_fields = ['subject']


class TagInlineAdmin(admin.StackedInline):
    model= Lesson.tags.through



class LessonAdmin(admin.ModelAdmin):
    form =LessonForm
    list_display = ['id','subject','create_day']
    inlines= [TagInlineAdmin,]



admin.site.register(Category)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Tag)




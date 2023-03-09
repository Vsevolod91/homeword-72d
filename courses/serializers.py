from rest_framework import serializers
from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('title', 'annotation', 'content', 'picture')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title','annotation', 'content', 'picture', 'link_movie')
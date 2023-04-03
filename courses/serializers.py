from rest_framework import serializers
from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = (
            'title',
            'annotation',
            'content',
            'picture',
            'link_movie',
        )


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='title_set', many=True)

    #lessons = serializers.SerializerMethodField('get_lessons')

    # def get_lessons(self, instance):
    #     lessons = Lesson.objects.all().filter(course=instance)
    #
    #     if lessons:
    #         return lessons
    #
    #     return 0

    class Meta:
        model = Course
        fields = (
            'title',
            'annotation',
            'content',
            'picture',
            'lessons',
        )


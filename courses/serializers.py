from rest_framework import serializers
from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    relate_lessons = serializers.SerializerMethodField('get_relate_lessons')

    def get_relate_lessons(self, instance):
        lessons = Lesson.objects.all().filter(course=instance)

        if lessons:
            return lessons

        return 0

    class Meta:
        model = Course
        fields = (
            'title',
            'annotation',
            'content',
            'picture',
            'relate_lessons',
        )


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


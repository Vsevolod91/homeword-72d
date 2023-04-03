from django.core.management import BaseCommand

from courses.models import Course, Lesson, Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):

        users = [
            {'email': 'marybloodmaria@yandex.ru', 'password': 'iamuserskyeducation8907'},
            {'email': 'verakontenova@yandex.ru', 'password': 'iamuserskyeducation8907'},
            {'email': 'korchenkov.d@yandex.ru', 'password': 'iamuserskyeducation8907'},
            {'email': 'vitalibashckatoff@yandex.ru', 'password': 'iamuserskyeducation8907'},
        ]

        users_to_db = []
        count = 0
        for item in users:
            count += 1
            if count <= 2:
                users_to_db.append(User(email=item['email'], password=item['password'], role=User.AUTHOR))
            else:
                users_to_db.append(User(email=item['email'], password=item['password'], role=User.CUSTOMER))

        User.objects.bulk_create(users_to_db)

        courses = [
            {
                'author': User.objects.all().get(id=1), 'title': 'Python-developer1',
                'annotation': 'Become a python-developer1'
            },
            {
                'author': User.objects.all().get(id=1), 'title': 'Python-developer2',
                'annotation': 'Become a python-developer2'
            },
            {
                'author': User.objects.all().get(id=2), 'title': 'SMM-specialist1',
                'annotation': 'Become a smm-specialist1'
            },
            {
                'author': User.objects.all().get(id=2), 'title': 'SMM-specialist2',
                'annotation': 'Become a smm-specialist2'
            }
        ]

        course_to_db = []
        for item in courses:
            course_to_db.append(Course(author=item['author'], title=item['title'], annotation=item['annotation']))

        Course.objects.bulk_create(course_to_db)

        lessons = [
            {
                'author': User.objects.all().get(id=1),
                'course': Course.objects.all().get(id=1),
                'title': 'Lesson', 'annotation': 'Hello World'
            },
            {
                'author': User.objects.all().get(id=1),
                'course': Course.objects.all().get(id=2),
                'title': 'Lesson', 'annotation': 'Hello World'
            },
            {
                'author': User.objects.all().get(id=2),
                'course': Course.objects.all().get(id=3),
                'title': 'Lesson', 'annotation': 'Hello World'
            },
            {
                'author': User.objects.all().get(id=2),
                'course': Course.objects.all().get(id=4),
                'title': 'Lesson', 'annotation': 'Hello World'
            }
        ]

        lessons_to_bd = []
        for item in lessons:
            lessons_to_bd.append(Lesson(author=item['author'], course=item['course'], title=item['title'], annotation=item['annotation']))

        Lesson.objects.bulk_create(lessons_to_bd)

        payments = [
            {
                'customer': User.objects.all().get(id=3),
                'course': Course.objects.all().get(id=1),
                'type': Payment.CASH, 'amount': 10500,
            },
            {
                'customer': User.objects.all().get(id=4),
                'course': Course.objects.all().get(id=2),
                'type': Payment.CASHLESS, 'amount': 21000,
            },
            {
                'customer': User.objects.all().get(id=3),
                'course': Course.objects.all().get(id=1),
                'type': Payment.CASH, 'amount': 10500,
            },
            {
                'customer': User.objects.all().get(id=4),
                'course': Course.objects.all().get(id=2),
                'type': Payment.CASHLESS, 'amount': 21000,
            },
            {
                'customer': User.objects.all().get(id=3),
                'course': Course.objects.all().get(id=1),
                'type': Payment.CASH, 'amount': 10500,
            },
            {
                'customer': User.objects.all().get(id=4),
                'course': Course.objects.all().get(id=2),
                'type': Payment.CASHLESS, 'amount': 21000,
            },
        ]

        payments_to_db = []
        for item in payments:
            payments_to_db.append(Payment(customer=item['customer'], course=item['course'],
                                          type=item['type'], amount=item['amount']))

        Payment.objects.bulk_create(payments_to_db)
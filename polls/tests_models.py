import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from faker import Faker


# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        faker_instance = Faker().date()
        # time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=faker_instance)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_questions(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_questions(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

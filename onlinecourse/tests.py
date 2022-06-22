import unittest
from django.test import TestCase

class TestCorrectAnswers(TestCase):

    def test1(self):

        # Database populated with 4 correct answers
        # Test for 4 correct answers
        self.assertEqual(Choice.Objects.filter(is_correct = True).count(), 4)

        # Database populated with 4 correct answers
        # Test that not all 8 choices are correct answers
        self.assertNotEqual(Choice.Objects.filter(is_correct = True).count(), 8)

class TestIncorrectAnswers(TestCase):

    def test1(self):

        # Database populated with 4 incorrect answers
        # Test for 4 incorrect answers
        self.assertEqual(Choice.Objects.filter(is_correct = False).count(), 4)

        # Database populated with 4 incorrect answers
        # Test that not all 8 choices are incorrect answers
        self.assertNotEqual(Choice.Objects.filter(is_correct = True).count(), 8)

unittest.main()
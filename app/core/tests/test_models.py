from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Module for testing model operations """

    def test_create_user_with_email_successful(self):
        """ test successful creation of user with email"""
        email = 'test@email.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test user email is normalized"""
        email = "test@ANDELA.COM"
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_email_not_provided_error(self):
        """value error if email is not provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '244344')

    def test_create_super_user(self):
        """Test creation of new super user"""
        user = get_user_model().objects.create_superuser('ty@gmail.com', '12')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

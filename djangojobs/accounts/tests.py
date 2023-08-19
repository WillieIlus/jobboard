from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        Profile.objects.create(
            user=self.user,
            bio='test bio',
            location='test location',
            birth_date='2021-01-01',
            profile_pic='test.jpg'
        )

    def test_profile_content(self):
        profile = Profile.objects.get(id=1)
        expected_user = f'{profile.user}'
        expected_bio = f'{profile.bio}'
        expected_location = f'{profile.location}'
        expected_birth_date = f'{profile.birth_date}'
        expected_profile_pic = f'{profile.profile_pic}'
        self.assertEqual(expected_user, 'testuser')
        self.assertEqual(expected_bio, 'test bio')
        self.assertEqual(expected_location, 'test location')
        self.assertEqual(expected_birth_date, '2021-01-01')
        self.assertEqual(expected_profile_pic, 'test.jpg')

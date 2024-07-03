from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from core.models import Posts, UserProfile, Vote


class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_superuser("username")

        # Create sample upvote
        self.sample_upvote = Vote.objects.create(
            type="upvote",
            ownerUserId=1,
            parentId=1,
            createdAt="2024-06-26 02:20:58.689998+00:00",
        )

        # Create sample downvote
        self.sample_downvote = Vote.objects.create(
            type="downvote",
            ownerUserId=1,
            parentId=1,
            createdAt="2024-06-26 02:20:58.689998+00:00",
        )

        self.sample_post = Posts.objects.create(
            type="argument",
            createdAt="2024-06-26 02:20:58.689998+00:00",
            updatedAt="2024-06-26 02:20:58.689998+00:00",
            body="<p>Sample post content</p>",
            ownerUserId=1,
            title="Sample Title",
        )

        # Create sample user profile
        self.sample_user_profile = UserProfile.objects.create(
            user=user,
            username="username",
            avatar="avatar",
            bio="bio",
            reputation=1,
            joinDate="2024-01-01",
            posts=self.sample_post,
            saved_posts=self.sample_post,
            private_post=self.sample_post,
            upvotes=self.sample_upvote,
            downvotes=self.sample_downvote,
        )
        # Correctly assign the edits to the user profile
        self.sample_user_profile.edits.set([self.sample_post])

    def test_user_profile_api(self):
        # Test the user profile API endpoint
        response = self.client.get(reverse("user-profile-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.sample_user_profile.username)

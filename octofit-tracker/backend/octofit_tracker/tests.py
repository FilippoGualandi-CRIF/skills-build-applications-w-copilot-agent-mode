from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Run', user='testuser', team='Test Team')
        self.assertEqual(str(activity), 'Run by testuser (Test Team)')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(str(lb), 'Test Team: 100')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', difficulty='Medium')
        self.assertEqual(str(workout), 'Pushups (Medium)')

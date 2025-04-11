from django.db import models
from accounts.models import User

class MembershipApplication(models.Model):
    INTEREST_CHOICES = [
        ('caring', 'Caring'),
        ('sharing', 'Sharing'),
        ('creating', 'Creating'),
        ('experiencing', 'Experiencing'),
        ('working', 'Working'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_interest = models.CharField(max_length=200)  # store comma-separated interests
    hobbies_passions = models.TextField()
    join_reason = models.TextField()
    contribution_method = models.TextField()
    member_goals = models.TextField()
    participation_frequency = models.TextField()  # changed from choice to free text
    accessibility_needs = models.TextField(blank=True, null=True)
    wants_newsletter = models.BooleanField()
    passionate_causes = models.TextField()
    event_ideas = models.TextField()
    previous_projects = models.TextField()
    six_month_contribution = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending') 
    membership_type = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.user.username}'s Application"
    





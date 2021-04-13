from django.db import models

# Create your models here.


class Contributor(models.Model):
    name = models.CharField(max_length=64, null=False)
    github_id = models.CharField(max_length=64, null=True, blank=True)
    fb_id = models.CharField(max_length=64, null=True, blank=True)
    twitter_id = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)

    def get_all_contributors(self):
        cons = list(Contributor.objects.all())
        return cons

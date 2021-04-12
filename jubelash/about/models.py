from django.db import models

# Create your models here.


class AboutModel(models.Model):
    def get_contributers_list(self):
        return [
            {
                'name': 'Ram',
                'github_handle': '',
                'fb_id': '',
                'twitter_id': ''
            },
            {
                'name': 'Sita',
                'github_handle': '',
                'fb_id': '',
                'twitter_id': ''
            },
            {
                'name': 'Hari',
                'github_handle': '',
                'fb_id': '',
                'twitter_id': ''
            }
        ]

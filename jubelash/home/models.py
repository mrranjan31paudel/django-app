from django.db import models
from datetime import datetime

# Create your models here.


class HomeModel(models.Model):
    def get_display_time_now(self):
        now = datetime.now()

        return now.strftime('%A, %B %d %Y, %I:%M:%S %p')

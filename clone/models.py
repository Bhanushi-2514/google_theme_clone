from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100)
    css_file = models.CharField(max_length=100)

    def __str__(self):
        return self.name


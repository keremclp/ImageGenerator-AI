from django.db import models

# Create your models here.


class Images(models.Model):
    phrase = models.CharField(max_length=200)
    ai_image = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.phrase)

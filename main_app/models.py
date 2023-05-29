from django.db import models

class EnderecoWeb(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url

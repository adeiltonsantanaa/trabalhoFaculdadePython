from django.db import models

class EnderecoWeb(models.Model):
    url = models.URLField()
    validacao = models.CharField(max_length=2, default='⚪')

    def __str__(self):
        return self.url

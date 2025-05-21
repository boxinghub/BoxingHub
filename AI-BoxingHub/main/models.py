from django.db import models

# Create your models here.
class BoxingHub(models.Model):
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField()
    loves = models.IntegerField()

    def __str__(self):
        return f'BoxingHub(id={self.id}, likes={self.likes}, loves={self.loves})'

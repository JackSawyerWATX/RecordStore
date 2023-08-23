from django.db import models

class Record(models.Model):
  artist = models.CharField(max_length=255)
  album = models.CharField(max_length=255)
  record_label = models.CharField(max_length=255, null=True)
  released = models.DateField(null=True)

  def __str__(self):
    return f"{self.artist} {self.album}"
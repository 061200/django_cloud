from django.db import models


class Cloud(models.Model):
    name = models.CharField(max_length=70)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

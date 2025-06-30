from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
def get_default_role():
    try:
        return Role.objects.get(name='learner').id
    except Role.DoesNotExist:
        return None

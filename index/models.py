from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Form(models.Model):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=100, default="#272124")


from django.db import models

class MyModel(models.Model):
    my_field = models.AutoField(primary_key=True)
    
    
class MyAutoField(models.AutoField):
    def __init__(self, start_at=1, increment_by=1, *args, **kwargs):
        self.start_at = start_at
        self.increment_by = increment_by
        super().__init__(*args, **kwargs)

    def get_next_value(self, *args, **kwargs):
        if self.model.objects.exists():
            max_value = self.model.objects.aggregate(models.Max(self.attname))[
                f"{self.attname}__max"
            ]
            if max_value is not None:
                return max_value + self.increment_by
        return self.start_at    
    
class MyModel(models.Model):
    my_field = MyAutoField(primary_key=True)    
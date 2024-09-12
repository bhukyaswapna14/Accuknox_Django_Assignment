import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_post_save_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.get_ident()}")

def save_model_instance():
    print(f"Caller running in thread: {threading.get_ident()}")
    instance = MyModel(name="Test Instance")
    instance.save()

save_model_instance()
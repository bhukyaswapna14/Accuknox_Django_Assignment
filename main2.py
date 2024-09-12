from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_post_save_handler(sender, instance, **kwargs):
    print("Signal handler running.")
    raise Exception("Error in signal handler!")


def save_model_instance():
    try:
        with transaction.atomic():
            instance = MyModel(name="Test Instance")
            instance.save()
            print("Model instance saved.")
    except Exception as e:
        print(f"Exception caught: {e}")

    print("Checking if the instance was saved in the database...")
    instance_exists = MyModel.objects.filter(name="Test Instance").exists()
    return instance_exists


was_saved = save_model_instance()
print(f"Was the instance saved? {was_saved}")


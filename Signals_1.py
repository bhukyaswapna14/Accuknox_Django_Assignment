#Topic: Django Signals - 1 question


#This behavior shows that Django signals are executed synchronously by default, as the sender waits for the receiver to finish its task before continuing.

import time
from django.dispatch import receiver, Signal


my_signal = Signal()


@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Signal received, processing...")
    time.sleep(5)
    print("Signal processing complete.")


print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent.")

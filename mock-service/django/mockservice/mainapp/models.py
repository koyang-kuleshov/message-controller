from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    number_of_message = models.IntegerField(
            null=True,
            editable=False,
            )

    def __str__(self):
        return f"{self.user} - {self.created_at}"


@receiver(post_save, sender=Message)
def update_number_of_message(sender, instance, **kwargs):
    number = len(instance.body) // 10 or 1
    sender.objects.filter(pk=instance.pk).update(number_of_message=number)

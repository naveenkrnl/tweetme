from django.urls import reverse
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent=parent_obj
        qs=self.get_queryset().filter(parent=og_parent).filter(
            timestamp__year=timezone.now().year,
            timestamp__month=timezone.now().month,
            timestamp__day=timezone.now().day,
            )
        if qs.exists():
            return None
        obj=self.model(
            parent=og_parent,
            user=user,
            content=og_parent.content,
        )
        obj.save()
        return obj
class Tweet(models.Model):
    parent=models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=0)
    content = models.CharField(max_length=140)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = TweetManager()
    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})
    class Meta:
        ordering = ['-timestamp']
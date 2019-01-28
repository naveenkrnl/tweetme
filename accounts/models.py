from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy
# Create your models here.
class UserProfileManager(models.Manager):
    use_for_related_fields=True
    def all(self):
        qs= self.get_queryset().all()
        try:
            if self.instance:
                qs=qs.exclude(user=self.instance)
        except:
            pass       
        return qs
    def toggle_follow(self, user, to_toggle_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user) #(user_obj, true)
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            added=False
        else:
            user_profile.following.add(to_toggle_user)
            added=True
        return added
    def is_following(self, user, followed_by_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user) #(user_obj, true)
        if created:
            return False
        if followed_by_user in user_profile.following.all():
            return True
        else:
            return False
        




class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=None)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
    
    
    objects = UserProfileManager()
    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        return self.following.all().exclude(username=self.user.username)
    def get_follow_url():
        return reverse_lazy("profiles:follow", kwargs={"username":self.user.username})
    def get_absolute_url():
        return reverse_lazy("profiles:detail", kwargs={"username":self.user.username})

def post_save_user_reciever(sender, instance, created, *args, **kwargs):
    if created:
        new_profile =UserProfile.objects.get_or_create(user=instance)
    #deffered tasks

post_save.connect(post_save_user_reciever, sender=settings.AUTH_USER_MODEL)
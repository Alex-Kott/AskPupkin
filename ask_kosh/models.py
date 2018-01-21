from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Answer(models.Model):
	question_id = models.IntegerField()
	text = models.TextField()
	user_id = models.IntegerField()


class Question(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField()
	tags = models.TextField()
	correst_question_id = models.OneToOneField(Answer, on_delete=models.CASCADE)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	userpic = models.TextField(default='/static/app/userpic.png')

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()


class Tag(models.Model):
	title = models.CharField(max_length=50)
	question = models.ManyToManyField(Question)



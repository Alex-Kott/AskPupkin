from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver






class Question(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField()
	tags = models.TextField()
	# correсt_answer = models.OneToOneField(Answer, on_delete=models.CASCADE, null=True)




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


class Answer(models.Model):
	text = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, default=0)

class Tag(models.Model):
	title = models.CharField(max_length=50)
	question = models.ManyToManyField(Question)



from django.db import models

# Create your models here.


# class User(models.Model):
# 	username = models.CharField(max_length=30)
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	email = models.CharField()
# 	password = models.CharField()
# 	is_staff = models.BooleanField()
# 	is_active = models.BooleanField()
# 	is_superuser = models.BooleanField()
# 	last_login = models.DateTimeField()
# 	data_joined = models.DateTimeField()


class Question(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField()
	tags = models.TextField()
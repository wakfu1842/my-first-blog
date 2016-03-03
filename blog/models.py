from django.db import models
# 2016-03-03 hbw
from django.utils import timezone

class Post(models.Model):
	"""docstring for Post"""
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title

	#def __init__(self, arg):
	#	super(Post, self).__init__()
	#	self.arg = arg
		

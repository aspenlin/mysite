from django.db import models
from django.utils import timezone

import datetime

class BlogCategory(models.Model):
	category = models.CharField(max_length=200)
	summary = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Blog Categories'

	def __str__(self):
		return self.category

class Blogs(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField('date published')
	category = models.ForeignKey(BlogCategory, default=1, verbose_name='Categories', on_delete=models.SET_DEFAULT)

	class Meta:
		verbose_name_plural = 'Blogs'
	
	def __str__(self):
		return self.title

class PhotoGallery(models.Model):
	photo = models.ImageField(upload_to='upload/gallery/%Y')
	filename = models.CharField(max_length=200)
	description = models.CharField(max_length=200, blank=True)
	pub_date = models.DateTimeField('date published')

	class Meta:
		verbose_name_plural = 'Gallery'
	
	def __str__(self):
		return self.filename

class CalliCategory(models.Model):
	category = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Calligraphy Categories'

	def __str__(self):
		return self.category

class Calligraphy(models.Model):
	photo = models.ImageField(upload_to='upload/calligraphy/%Y')
	description = models.CharField(max_length=200)
	filename = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	category = models.ForeignKey(CalliCategory, default=1, verbose_name='Categories', on_delete=models.SET_DEFAULT)

	class Meta:
		verbose_name_plural = 'Calligraphy'

	def __str__(self):
		return self.filename







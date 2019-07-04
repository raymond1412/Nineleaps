from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=120)
	designation = models.CharField(max_length=120)
	manager = models.CharField(max_length=120,blank=True)
	parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE,related_name='children')
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ["id"]
from django.db import models
from django.contrib.auth.models import User
class TableData(models.Model):
	table_name=models.CharField(max_length=100)
	table_desc=models.TextField(default="")
	table_owner=models.ForeignKey(User)
	table_data=models.TextField(default="")
	def __unicode__(self):
		return unicode(self.table_name)


class GroupData(models.Model):
	group_name = models.CharField(max_length=100)
	group_desc=models.TextField(default="")
	group_members = models.ManyToManyField(User)
	def __unicode__(self):
		return unicode(self.group_name)

class GroupAdminInfo(models.Model):
	group_name=models.ForeignKey(GroupData)
	group_admin=models.ForeignKey(User)
	entry_id=models.AutoField(primary_key = True)
	def __unicode__(self):
		return unicode(self.entry_id)

class TableOwnerInfo(models.Model):
	group_name=models.ForeignKey(GroupData)
	table_name=models.ForeignKey(TableData)
	table_owner=models.ForeignKey(User)

	def __unicode__(self):
		return unicode(self.id)











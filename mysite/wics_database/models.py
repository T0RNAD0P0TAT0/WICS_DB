from django.db import models

# Create your models here.
# Models contain the essential fields and behaviors
# of the data you're storing.

class wicsMember(models.Model):
	yearInSchoolChoices = (
		('1U', '1st Year Undergrad'),
		('2U', '2nd Year Undergrad'),
		('3U', '3rd Year Undergrad'),
		('4U', '4th Year Undergrad'),
		('5U', '5th Year Undergrad'),
		('U++', '5+th Year Undergrad'),
		('GR', 'Graduate'),
	)
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50, primary_key = True)
	yearInCollege = models.CharField(max_length = 3, choices = yearInSchoolChoices)
	major = models.CharField(max_length = 50)
	mostRecentMeetingDate = models.CharField(max_length = 50)
		#todo: use DateTimeField for timedates
	numMeetingsAttended = models.IntegerField(default = 0)
	# sex or gender #todo make it go from female, male, other
	identifiedGender = models.CharField(max_length = 50)

	def get_all_members(self):
		return self.objects.all()
	def __str__(self):
		return self.firstName + ' ' + self.lastName
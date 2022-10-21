from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group




def customer_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='customer')
		instance.groups.add(group)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)
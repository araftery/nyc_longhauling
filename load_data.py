from db.models import *
user = User(name="Dan", email="dancaron@gmail.com")
user.save()

sample_user = User.objects.all()[0]

print sample_user.name
print sample_user.email

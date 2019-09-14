from django.db import models
from django.contrib.auth.models import User  # so that we can use User in hunter element

class Cool(models.Model):
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
  #  date = models.DateField(auto_now=False)
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
   
    def _str_(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


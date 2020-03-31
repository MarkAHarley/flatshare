import uuid
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User




class Flat(models.Model):
    flat_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    address = models.CharField(max_length=30, default = "1")
    postcode = models.CharField(max_length=10, default = "1")
    rent = models.IntegerField(default=1)
    description = models.TextField(max_length=500,default = "123")
    available_from = models.DateField(default=now)
    #image = models.ImageField(upload_to=str(flat_id)+'_images', blank=True) #will be replaced by a gallery soon

    #owner = models.OneToOneField("UserProfile", on_delete=models.CASCADE)

    likes = models.ManyToManyField('Like')
    matches = models.ManyToManyField('Match')
    

    def __str__(self):
        return self.address


class UserProfile(models.Model):
    NAME_MAX_CHAR = 128
    user_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    FirstName = models.CharField(max_length=NAME_MAX_CHAR, unique=False)
    LastName = models.CharField(max_length=NAME_MAX_CHAR, unique=False)
    email = models.CharField(max_length=30, unique=True)
    course = models.CharField(max_length=30, unique=False)
    location = models.CharField(max_length=128, unique=False)
    bio = models.CharField(max_length = 200, unique=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone_no = models.IntegerField(default=888, unique=True)
    age = models.IntegerField(default=18)

    u_flat = models.OneToOneField(Flat, on_delete=models.CASCADE,default=None, null = True)

    likes = models.ManyToManyField('Like')
    matches = models.ManyToManyField('Match')

    def __str__(self):
        return self.FirstName + " " + self.LastName




class Match(models.Model):
    match_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    m_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    m_flat = models.ForeignKey(Flat, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Matches'

class Like(models.Model):
    like_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    direction_flag = models.BooleanField(default=True) #True = user likes flat
    l_flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    l_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    

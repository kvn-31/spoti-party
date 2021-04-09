from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        # will generate a random code at k length
        code = ''.join(random.choices(string.ascii_uppercase, k=length))        
        # counts all objects that meet criteria -> would be possible to use exists()
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=2)
    created_at = models.DateTimeField(auto_now_add=True) # will automatically add time when room is created
    current_song = models.CharField(max_length=50, null=True)


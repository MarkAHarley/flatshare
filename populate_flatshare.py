import os
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE','flatshare_project.settings')

import django
django.setup()
from flatshare.models import UserProfile, Flat, Like, Match

def populate():

    flats = [
        {'address': '46 Bentinck Street',
         'postcode': 'G37TT',
         'rent':490,
         'description':'5 Person flat close to GU',
         'owner': None,
         'likes': None,
         'matches':None,
         },
        {'address': '23 Bentinck Street',
         'postcode': 'G38TT',
         'rent':600,
         'description':'2 Person flat close to GU',
         'owner': None,
         'likes': None,
         'matches':None,
         },
        {'address': '25 Hillhead Street',
         'postcode': 'G26TR',
         'rent':490,
         'description':'4 Person flat close to GU',
         'owner': None,
         'likes': None,
         'matches':None,
         },
        ]

    users = [
        {'FirstName':'Mark',
         'LastName':'Harley',
         'email':'2378551H@student.gla.ac.uk',
         'course':'ESE',
         'location': 'Glasgow',
         'bio':'Engineering Student who plays a lot of music',
         'flat': flats[0],
         'likes':None,
         'matches':None,
         'phone':123
         },
        {'FirstName':'Adam',
         'LastName':'Simpson',
         'email':'2378433S@student.gla.ac.uk',
         'course':'Geography',
         'location': 'Glasgow',
         'bio':'wwww',
         'flat': flats[1],
         'likes':None,
         'matches':None,
         'phone':1234567
         },
        {'FirstName':'Neil',
         'LastName':'Campbell',
         'email':'2466521@student.gla.ac.uk',
         'course':'History',
         'location': 'Glasgow',
         'bio':'aaaaa',
         'flat': flats[2],
         'likes':None,
         'matches':None,
         'phone':12345
         },
        {'FirstName':'Douglas',
         'LastName':'Russell',
         'email':'1234556R@student.gla.ac.uk',
         'course':'ESE',
         'location': 'Glasgow',
         'bio':'Engineering Student',
         'flat': None,
         'likes':None,
         'matches':None,
         'phone':12345678
         },
        {'FirstName':'Matthew',
         'LastName':'Harrison',
         'email':'2378561H@student.gla.ac.uk',
         'course':'Medicine',
         'location': 'Glasgow',
         'bio':'Medic',
         'flat': None,
         'likes':None,
         'matches':None,
         'phone':432
         },
        ]

    ##GOING TO ADD LIKES HERE AND AUTOMATIC MATCH DETECTION ELSEWHERE LATER

    

    for user in users:
        if user['flat'] != None:
            u = add_user(user['FirstName'],user['LastName'],user['email'],user['course'],
                         user['location'],user['bio'],user['likes'],user['matches'],user['phone'],
                         flat = add_flat(user['flat']['address'],user['flat']['postcode'],
                                        user['flat']['rent'], user['flat']['description']))
        else:
            u = add_user(user['FirstName'],user['LastName'],user['email'],user['course'],
                         user['location'],user['bio'],user['likes'],user['matches'],user['phone'])

    


def add_flat(address, postcode, rent, description):
         f = Flat.objects.get_or_create(flat_id = uuid.uuid4())[0]
         f.address = address
         f.postcode=postcode
         f.rent=rent
         f.description=description

         f.save()
         return f

def add_user(FirstName, LastName, email, course, location, bio, likes, matches, phone_no, flat = None):
         u = UserProfile.objects.get_or_create(user_id = uuid.uuid4(),phone_no = phone_no,email=email)[0]
         #u.likes.set(likes)
         #u.matches.set(matches)
         u.flat = flat
         u.FirstName = FirstName
         u.LastName = LastName
         u.email = email
         u.course = course
         u.location = location
         u.bio = bio

         u.save()
         return u

def add_like(flat, user, flag = True):
         l = Like.objects.get_or_create(like_id = uuid.uuid4())
         l.l_flat = flat
         l.l_user = user
         l.directionflag = flag

         l.save()
         return l

def add_match(flat, user):
         m = Match.objects.get_or_create(match_id = uuid.uuid4())
         m.m_flat = flat
         m.m_user = user

         m.save()
         return m

if __name__ == '__main__':
    print("Starting flatshare population...")
    populate()
         

from django import forms
from django.utils.timezone import now
from flatshare.models import Flat,Like, Match, UserProfile
from django.contrib.auth.models import User

'''
class AddAddressForm(forms.ModelForm):
    help_text=("Please enter an address for your flat")
    flat_no = forms.CharField()
    house_no = forms.IntegerField()
    street = forms.CharField()
    city = forms.CharField()
    province = forms.CharField()
    postcode = forms.CharField()
    country = forms.CharField()

    class Meta:
        model = Address
        fields = ('flat_no','house_no', 'street', 'city', 'province', 'postcode', 'country')
'''

class AddFlatForm(forms.ModelForm,):
    help_text = ("Please enter flat details.")
    name = forms.CharField()
    rent = forms.IntegerField(initial=0)
    address = forms.CharField()
    description = forms.TextInput()
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    available_from = forms.DateField(initial=now())
    #likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Flat
        fields = ('name', 'rent','address', 'description', 'image1', 'image2', 'available_from')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User
        fields = ('username', 'email', 'password',)
        
class UserProfileForm(forms.ModelForm): 
    class Meta:
        model = UserProfile
        fields = ('FirstName', 'LastName', 'picture','course','location','bio', 'phone_no', 'age')

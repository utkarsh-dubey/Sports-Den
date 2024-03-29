from django import forms
from .models import Post,Comment,Going,Profile, Interest
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required = False, help_text='optional')
    location = forms.CharField(max_length=20, required = True, help_text='Required')
    birth_date = forms.DateField(required = False, help_text='optional, Format: YYYY-MM-DD')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'location', 'birth_date', 'password1', 'password2', )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up', 'Sign up', css_class = 'btn-primary'))
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password',)



class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ["title", "user","location","content", "category"]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ['image', 'bio', 'location']

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class Goingform(forms.ModelForm):

    class Meta:
        model = Going
        fields = ('name','going')
        widgets = {
            'going': forms.Select(choices=TRUE_FALSE_CHOICES)
        }

class InterestForm(forms.ModelForm):

    category = ('pubg', 'Pubg'),('basketball', 'Basketball'),('football', 'Football'),('cricket', 'Cricket')

    interests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                  choices=category)

    class Meta:
        model = Interest
        fields = ('interests',  )

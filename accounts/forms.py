from django.contrib.auth.forms import UserCreationForm
from .models import Member

class MemberForm(UserCreationForm):

    class Meta:
        model = Member
        fields = ('username', 'email', 'password1', 'password2', 'profile_pic', 'about', 'website')

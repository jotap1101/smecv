from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

# Create your forms here.
User = get_user_model()

class UserLoginForm(AuthenticationForm):
    pass

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'password' in self.fields:
            self.fields.pop('password')
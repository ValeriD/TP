from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth.models import User

def authenticateUser(username, password):
    try:
        user = User.objects.get(username=username)
        return user.check_password(password)
    except:
        return False

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        authenticated = authenticateUser(username, password)
        if(not authenticated and username is not None and password is not None):
            #authentication attempted and failed
            raise exceptions.AuthenticationFailed('Username/password pair not found')
        elif(not authenticated):
            #authentication not attempted (try other authentications)
            return None
        else:
            #authentication attempted and suceeded
            return (User.objects.get(username=username), None)


    def authenticate_header(self, request):
        return '{"username" : <username>, "password" : <password>}'

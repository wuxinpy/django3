from django.contrib.auth.models import User

class EmailAuthBackend(object):
    def authenticate(self, request, username=None, password=None):  # username和password 是表格填写的内容
        try:
            user = User.objects.get(email=username)
            print(username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
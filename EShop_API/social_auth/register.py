import os
import random

from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from users.models import User


def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            print(os.environ.get('SOCIAL_SECRET'))
            registered_user = auth.authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))
            print(registered_user)
            return {
                'username': name,
                'email': email}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': os.environ.get('SOCIAL_SECRET')}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }

from django.contrib.auth import get_user_model
import requests
from django.core.files.base import ContentFile

User = get_user_model()

def get_user_by_email(strategy, details, backend, *args, **kwargs):
    email = details.get('email')
    if email:
        try:
            user = User.objects.get(email=email)
            return {'user': user}
        except User.DoesNotExist:
            return None
    return None

def save_profile_picture(strategy, details, user=None, *args, **kwargs):
    if user and not user.profile_picture:
        picture_url = kwargs.get('response', {}).get('picture')
        if picture_url:
            try:
                response = requests.get(picture_url)
                if response.status_code == 200:
                    file_name = f"{user.id}_google.jpg"
                    print(f"Saved profile Pic: {file_name}")
                    user.profile_picture.save(file_name, ContentFile(response.content), save=True)
            except Exception as e:
                # Optional: log error or fail silently
                print(f"Failed to fetch profile picture: {e}")
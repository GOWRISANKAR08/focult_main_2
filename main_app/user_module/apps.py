# user_module/apps.py
from django.apps import AppConfig

class UserModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app.user_module'  # Full Python path
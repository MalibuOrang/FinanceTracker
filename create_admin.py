import os
import django

# Указываем путь к настройкам вашего проекта
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "finance_project.settings"
)  # замените my_project на имя вашего проекта

# Инициализируем Django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "yourpassword")
    print("Admin user created")
else:
    print("Admin user already exists")

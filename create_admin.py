import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance_project.settings")
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "MrOrange*8004")
    print("Admin user created")
else:
    print("Admin user already exists")

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "MrOrange*8004")
    print("Admin user created")
else:
    print("Admin user already exists")

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_mgmt.settings')
django.setup()

from accounts.models import User

def check_users():
    users = User.objects.all()
    print(f"Total users: {users.count()}")
    for user in users:
        print(f"Username: {user.username}, Role: {user.role}, Is Superuser: {user.is_superuser}")

    # Create or update admin user
    admin_user, created = User.objects.get_or_create(username='admin')
    if created:
        admin_user.set_password('admin')
        admin_user.role = 'ADMIN'
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.save()
        print("Created 'admin' user with password 'admin'")
    else:
        if admin_user.role != 'ADMIN':
            admin_user.role = 'ADMIN'
            admin_user.save()
            print("Updated 'admin' user to have ADMIN role")
        else:
            print("'admin' user already exists and is ADMIN")

    # Promote 'test' user if exists
    try:
        test_user = User.objects.get(username='test')
        test_user.role = 'ADMIN'
        test_user.save()
        print("Promoted 'test' user to ADMIN")
    except User.DoesNotExist:
        pass

if __name__ == '__main__':
    check_users()

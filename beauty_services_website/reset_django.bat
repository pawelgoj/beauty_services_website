py manage.py makemigrations
py manage.py migrate 
py manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" 
ECHO Done!
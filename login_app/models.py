from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 3:
            errors['name'] = "Name must be 3 characters or more!"
        if len(post_data['last_name']) < 3:
            errors['alias'] = "Alias must be 3 characters or more!"
        if len(post_data['email']) < 8:
            errors['email'] = "Email must be 8 characters or more!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be 8 characters or more!"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm'] = "Passwords don't match!"
        return errors
    
    def login_validator(self, post_data):
        errors = {}
        if len(post_data['email']) < 8:
            errors['email'] = "Email must be 8 characters or more!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be 8 characters or more!"
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
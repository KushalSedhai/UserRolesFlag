from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email not registered")
        
        email = self.normalize_email(email)
        
        user = self.model(
            email = email,
            username=username
        )
            
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_agent(self,email, username, password=None):
        user = self.create_user(email, username, password)
        
        user.is_agent = True
        user.save(using = self._db)
        return user

    def create_superuser(self,email, username, password=None):
        user = self.create_user(email, username, password)
        
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using = self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    is_agent = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
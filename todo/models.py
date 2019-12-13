from datetime import datetime
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class PersonManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        """
            Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("User must have email or password")

        user = self.model(
            email=self.normalize_email(email),  
            first_name=first_name,
            last_name=last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
            Creates and save admin user with give email and passsword
        """
        if not email:
            raise ValueError("User must have email or password")

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.is_admin=True
        user.save(using=self._db)
        return user



class Person(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        max_length=255,
        blank=True,
        null=True,
        default="",        
    )

    is_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=100,null=True,blank=True,default="")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = PersonManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name",]

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return True

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


    

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.category_name



class List(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)






    

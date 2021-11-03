from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.utils.translation import gettext as _
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email,first_name, last_name, role, password=None,**other_fields):
        if not email:
            raise ValueError(_('You must provid an email adress'))
        

        email = self.normalize_email(email)
        user = self.model(email=email , first_name=first_name, last_name=last_name, role=role, **other_fields )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name, last_name, role, password=None,**other_fields):
        if role == 'instructor':

            other_fields.setdefault('is_staff', True)
            other_fields.setdefault('is_superuser', True)
            other_fields.setdefault('is_active', True)
        elif role == 'ta':
            other_fields.setdefault('is_staff', True)
            other_fields.setdefault('is_active', True)
        else:
            other_fields.setdefault('is_active', True)




        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email,first_name, last_name, role, password,**other_fields)







class User(AbstractBaseUser,PermissionsMixin):
    roles= [
        ('instructor', 'instructor'),
        ('ta', 'ta'),
        ('student', 'student'),
        
    ]
    email = models.EmailField(_('email adress'), unique=True, blank=False, max_length=255,)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    role = models.CharField(max_length=255, blank=False, default='student',choices=roles)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login' , auto_now = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'


    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return (f'{self.first_name} {self.last_name}')

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, name, password, is_staff, is_superuser=False, **extra_fields):
        user = self.model(
            email=email,
            name=name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, email, name, password, **extra_fields):
        return self._create_user(email, name, password, False, False, **extra_fields)

    def create_superuser(self, email, name, password, **extra_fields):
        return self._create_user(email, name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Nombre Completo', max_length=255, blank=True, null=True)
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True, )
    address = models.CharField('Direccion', max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    cellphone = models.IntegerField(blank=True, null=True)
    document_type = models.IntegerField(blank=True, null=True)
    document_number = models.IntegerField(blank=True, null=True)  # 1 - DNI, 2 - RUC, 3 - Carnet de Extranjeria
    is_provider = models.BooleanField(default=True)
    is_worker = models.BooleanField(default=True)
    is_client = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def str(self):
        return f'{self.name}'


class Permission(models.Model):
    path = models.CharField(max_length=256)
    status = models.BooleanField()

    class Meta:
        db_table = 'permission'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'Permission'  # Como se muestra papi
        verbose_name_plural = 'Permissions'  # ? :v

    # To String
    def __str__(self):
        return self.path


class Role(models.Model):
    name = models.CharField(max_length=156)
    status = models.BooleanField()
    #Symetrical solo registra una vez el id :'v
    permission = models.ManyToManyField(Permission, blank=True, symmetrical=False)

    class Meta:
        db_table = 'role'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'Role'  # Como se muestra papi
        verbose_name_plural = 'Roles'  # ? :v

    # To String
    def __str__(self):
        return self.name

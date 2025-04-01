from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.hashed_filename_generator import generate_hashed_filename
from uuid import uuid4
import os

# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username'),
            models.UniqueConstraint(fields=['email'], name='unique_email'),
        ]

    def get_path_to_profile_picture(instance, filename):
        return generate_hashed_filename(instance, 'users/profile_pictures', filename)
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    email = models.EmailField(max_length=255, unique=True, verbose_name='E-mail')
    profile_picture = models.ImageField(upload_to=get_path_to_profile_picture, blank=True, null=True, verbose_name='Foto de perfil')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = User.objects.get(pk=self.pk)

                if old_instance.profile_picture and self.profile_picture != old_instance.profile_picture:
                    if os.path.isfile(old_instance.profile_picture.path):
                        os.remove(old_instance.profile_picture.path)
            except User.DoesNotExist:
                pass
            
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.profile_picture:
            if os.path.isfile(self.profile_picture.path):
                os.remove(self.profile_picture.path)
        
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.get_full_name() or self.username
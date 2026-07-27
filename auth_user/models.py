from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from django.db.models import Max


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    TYPE_CODE_MAP = {
        'admin': '99',
        'teacher': '88',
        'student': '77',
    }
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    registration_no = models.CharField(max_length=15, unique=True, blank=True, null=True)

    def generate_registration_no(self):
        year = datetime.now().strftime('%Y')
        type_code = self.TYPE_CODE_MAP.get(self.user_type, '00')
        with transaction.atomic():
            last_reg = CustomUser.objects.filter(
                registration_no__startswith=year
            ).select_for_update().aggregate(Max('registration_no'))
            last_no = last_reg['registration_no__max']
            if last_no:
                sequence = int(last_no[-4:]) + 1
            else:
                sequence = 1
            return f'{year}{type_code}{sequence:04d}'

    def save(self, *args, **kwargs):
        if not self.registration_no:
            self.registration_no = self.generate_registration_no()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}"

from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from tabnanny import verbose
from time import sleep
from unicodedata import name
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from accounts.models import Account
from django.urls import reverse


class Dr(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'Drs'
    
    def __str__(self):
        return self.name

class Attendance(models.Model):
    dr = models.ForeignKey(Dr, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    date = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    qr_code = models.ImageField(upload_to='Attendance', blank=True)

    class Meta:
        verbose_name_plural = 'Attendance QR'

    def dr_name(self):
        return self.dr

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        qrcode_image = qrcode.make(self.url)
        create_image = Image.new('RGB', (370, 370), 'white')
        draw = ImageDraw.Draw(create_image)
        create_image.paste(qrcode_image)
        qr_name = f'qr_code-{self.date}.png'
        buffer = BytesIO()
        create_image.save(buffer, 'PNG')
        self.qr_code.save(qr_name, File(buffer), save=False)
        create_image.close()
        super().save(*args, **kwargs)

    
    def get_att_url(self):
        return reverse('home:attendance_list', args=[self.dr.slug, self.slug])


class Attendance_List(models.Model):
    dr = models.ForeignKey(Dr, on_delete=models.CASCADE)
    qrcode = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    loginid = models.CharField(max_length=100, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Attendance List'

    def __str__(self):
        return str(self.loginid)



class Leave(models.Model):
    dr = models.ForeignKey(Dr, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    date = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    qr_code = models.ImageField(upload_to='leave', blank=True)

    class Meta:
        verbose_name_plural = 'Leave QR'

    def dr_name(self):
        return self.dr

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        qrcode_image = qrcode.make(self.url)
        create_image = Image.new('RGB', (370, 370), 'white')
        draw = ImageDraw.Draw(create_image)
        create_image.paste(qrcode_image)
        qr_name = f'qr_code-{self.date}.png'
        buffer = BytesIO()
        create_image.save(buffer, 'PNG')
        self.qr_code.save(qr_name, File(buffer), save=False)
        create_image.close()
        super().save(*args, **kwargs)

    
    def get_leave_url(self):
        return reverse('home:leave_list', args=[self.dr.slug, self.slug])

class Leave_List(models.Model):
    dr = models.ForeignKey(Dr, on_delete=models.CASCADE)
    qrcode = models.ForeignKey(Leave, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    loginid = models.CharField(max_length=100, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Leave List'

    def __str__(self):
        return str(self.loginid)
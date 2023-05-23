from django.db import models


class Login(models.Model):
    """
    This class is for logging in users on the site
    """

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


SupportId = (
    ("بخش مالی (فاکتور/پیش فاکتور/بازگشت وجه)", "بخش مالی (فاکتور/پیش فاکتور/بازگشت وجه)"),
    ("خدمات پس از فروش (بازکشت کالا)", "خدمات پس از فروش (بازکشت کالا)"),
    ("پشتیبانی", "پشتیبانی"),
)

DegreeId = (
    ("کم", "کم"),
    ("متوسط", "متوسط"),
    ("فوری", "فوری"),
    ("بحرانی", "بحرانی"),
)


class LoginMessages(models.Model):
    """
    This class is for logging in users on the site
    """

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    support = models.CharField(choices=SupportId, max_length=255)
    degree = models.CharField(choices=DegreeId, max_length=255)
    file_field = models.FileField(upload_to='', storage=None, max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.username

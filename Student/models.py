from django.db import models

class Student(models.Model):
    s_fname = models.CharField(max_length=255)
    s_lname = models.CharField(max_length=255)
    s_gender = models.CharField(max_length=255)
    s_email = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.s_fname

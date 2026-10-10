from django.db import models

class ResumeModel(models.Model):
    full_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    summary = models.TextField(verbose_name="Short personal objective")
    degree = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    year_of_graduation = models.IntegerField()
    company_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    years_of_experience = models.IntegerField(default=0)
    skills = models.TextField(help_text="comma-separated")
    hobbies = models.TextField(help_text="comma-separated")
    achievements = models.TextField(help_text="comma-separated")

    def __str__(self):
        return self.full_name
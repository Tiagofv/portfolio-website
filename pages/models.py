from django.db import models
from datetime import datetime
from .validators import validatePdf
# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    email = models.CharField(max_length=200, blank=True)
    linked_in = models.URLField(max_length=300, blank=True)
    occupation = models.CharField(max_length=200, blank=True)
    currently_available = models.BooleanField(default=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d/', blank=True, validators = [validatePdf])
    hire_date = models.DateTimeField(blank=True)
    description = models.TextField()
    completed_projects = models.IntegerField(blank=True, default=1)
    satisfied_clients = models.IntegerField(blank=True, default=1)
    finished_projects = models.IntegerField(blank=True, default=1)
    def __str__(self):
        return self.name

class Projects(models.Model):
    dev = models.ForeignKey('Developer', on_delete=models.DO_NOTHING, blank=True, default = "1")
    title = models.CharField(max_length=200)
    tags = models.TextField(blank=True)
    description = models.TextField()
    project_date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)
    main_photo = models.ImageField(upload_to='projects/%Y/%m/%d/', blank=True)
    opt_photo_1 = models.ImageField(upload_to='projects/%Y/%m/%d/', blank=True)
    opt_photo_2 = models.ImageField(upload_to='projects/%Y/%m/%d/', blank=True)
    url = models.TextField( blank=True)

    def __str__(self):
        return self.title
    def get_tags(self):
        return self.tags.split(",")
class Work(models.Model):
    dev = models.ForeignKey('Developer', on_delete=models.DO_NOTHING, blank=True, default = "1")
    title = models.CharField(max_length=200, blank=True)
    occupation = models.CharField(max_length=200, blank=True)
    place = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    hire_date = models.DateTimeField(blank=True, null=True)
    hire_end_date = models.DateTimeField(blank=True, null=True)
    until_today = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Education(models.Model):
    dev = models.ForeignKey('Developer', on_delete=models.DO_NOTHING, blank=True, default = "1")
    type_of_graduation = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=200)
    course = models.CharField(max_length=255)
    begin_date = models.DateTimeField(blank=True)
    until_today = models.BooleanField(default=False)
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    def __str__(self):
        return self.course
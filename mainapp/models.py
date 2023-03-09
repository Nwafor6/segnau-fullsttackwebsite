from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(blank=True, null=True, help_text="Leave this blank.Auto fill enabled.")
    body=RichTextField()
    image=models.FileField()
    is_draft=models.BooleanField(default=True, help_text="Do not turn this to false if you haven't througly review your the aritcle")
    posted_on=models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Blog, self).save(*args,**kwargs)
		

class Newsletter(models.Model):
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return self.email


class   Membership(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    course_of_study=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    excepted_year_of_graduation=models.DateTimeField()
    address=models.CharField(max_length=100)
    date_of_birth=models.DateTimeField()
    gender=models.CharField(max_length=100, choices=(("Male","Male"),("Female", "Female"),( "Others", "others")))
    phone_number=models.CharField(max_length=20)
    payment_slip=models.ImageField(upload_to="payment_slip")

    def __str__(self):
        return self.full_name
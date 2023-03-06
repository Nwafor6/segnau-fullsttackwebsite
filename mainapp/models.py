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

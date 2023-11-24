from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255, null=True, blank= True)
    image=models.ImageField(upload_to="media/category")
    def __str__(self):
        return self.title
    class Meta:
      verbose_name="category"
      verbose_name_plural="categories"


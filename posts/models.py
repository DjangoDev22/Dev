from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title= models.CharField(max_length=200)
    content= models.TextField()
    image= models.ImageField(upload_to='post_image/', null=True, blank=True)
    slug= models.SlugField(null=True, blank=True)

    tags= models.ManyToManyField('Tags')
    category= models.ForeignKey('Categories', on_delete=models.CASCADE)

    created_at= models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(default=timezone.now)

    likes= models.ManyToManyField(User, default=None, blank=True, related_name="likes")
    dislikes= models.ManyToManyField(User, default=None, blank=True, related_name="dislikes")

    favourites= models.ManyToManyField(User, blank=True, related_name="favourites")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "Article"
        verbose_name_plural= "Articles"

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        return super().save(*args, **kwargs)


class Tags(models.Model):
    tag_name= models.CharField(max_length=20)
    slug= models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name= "Tag"
        verbose_name_plural= "Tags"

    def save(self, *args, **kwargs):
        self.slug= slugify(self.tag_name)
        return super(Tags, self).save(*args, **kwargs)


class Categories(models.Model):
    category_name= models.CharField(max_length=50)
    slug= models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name= "Category"
        verbose_name_plural= "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)

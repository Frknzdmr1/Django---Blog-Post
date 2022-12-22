from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=15)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    web_page = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to = "media/images", blank =True, null = True)
    GENDER_OPTIONS = [
        ('M', 'Male'),
        ('N', 'Not to sa'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length= 1, choices=GENDER_OPTIONS)

    def __str__(self):
        return f"{self.user}"


class Blog(models.Model):
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=20)
        content = models.TextField()
        time_stamp=models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return "f{self.title}"


class Likes(models.Model):
        time_stamp = models.DateTimeField(auto_now_add=True)
        blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
        user = models.ManyToManyField(User)

        def __str__(self):
            return f"{self.blog}"

class Meta:
    verbose_name_Plural = "Likes"
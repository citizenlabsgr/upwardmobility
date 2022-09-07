# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField
from django.urls import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text =  QuillField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    iframe_media = models.TextField(null=True, blank=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


class SubSection(models.Model):
    main_post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="sub_sections")
    sequence = models.PositiveSmallIntegerField()
    section_text = QuillField()
    visualization = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['sequence']

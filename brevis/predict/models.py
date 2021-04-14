from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from .summarizer import summarizer

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    body_summarized = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=False, unique=True) 
    text_len = models.PositiveIntegerField(null=True, blank=True)
    summary_len = models.PositiveIntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={ 'slug': self.slug })

    def summarize(self):
        if not self.body_summarized:
            print(f"Summarizing {self.title}")
            self.body_summarized = summarizer(self.body)
        if len(self.body_summarized) >1 :
            self.summary_len = len(self.body_summarized.split(" "))
        else:
            self.summary_len = len(self.body_summarized[0].split(" "))
        self.save()

    def save(self, *args, **kwargs): # new
        self.text_len = len(self.body.split(" "))
        if not self.slug:
            self.slug = slugify(self.title)
            print(self.slug)

        return super().save(*args, **kwargs)


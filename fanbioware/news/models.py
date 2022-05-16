from datetime import date
from django.db import models
from bioware.models import Game


class News(models.Model):
    """Creating the News model."""

    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, blank=True,
        null=True, related_name='news',
        verbose_name='Game',
        help_text='Choose the game',
    )
    title = models.CharField(
        max_length=45,
        verbose_name='Title',
        help_text='Enter a title of the news'
    )
    pub_date = models.DateField(default=date.today())
    intro = models.CharField(
        max_length=90,
        verbose_name='Intro',
        help_text='Enter a short intro of the news',
    )
    text = models.TextField(
        verbose_name='Text',
        help_text='Enter the news text'
    )
    image = models.ImageField(
        verbose_name='Cover',
        help_text='Attach the cover of the news',
        upload_to='bioware/news/',
    )
    is_publicated = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        """Return the title of the News."""
        return self.title

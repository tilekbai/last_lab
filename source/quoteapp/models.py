from django.db import models
from django.db.models.enums import Choices

STATUS_CHOICE = (
    ("новая", "новая"),
    ("модерированная", "модерированная")    
)

class Quote(models.Model):
    text = models.TextField(max_length=1000, blank=False, null=False, verbose_name="Текст")
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Имя")
    email = models.EmailField(blank=False, null=False, verbose_name="Email")
    rating = models.IntegerField(default=0, verbose_name="Рэйтинг")
    status = models.CharField(max_length=50, default="новая", choices=STATUS_CHOICE, verbose_name="Статус")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return f"<<<{self.id}-{self.text}-{self.name}>>>"


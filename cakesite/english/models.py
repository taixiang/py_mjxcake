from django.db import models


# Create your models here.

class learn(models.Model):
    title = models.CharField("标题", max_length=200, blank=True)
    time = models.DateField("时间", blank=True)
    content = models.TextField("内容", blank=True)
    url = models.CharField("链接", max_length=200, blank=True)
    audioUrl = models.CharField("听力", max_length=200, blank=True)

    class Meta:
        ordering = ("-time",)

    def __str__(self):
        return self.time.strftime("%Y-%m-%d")

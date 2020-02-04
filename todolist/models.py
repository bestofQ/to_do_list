from django.db import models

# Create your models here.


class Todo(models.Model):

    thing = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    # class Meta:
    #     verbose_name = "Todo"
    #     verbose_name_plural = "Todos"

    def __str__(self):
        pass
    
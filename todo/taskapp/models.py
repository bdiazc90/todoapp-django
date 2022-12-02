from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(editable=False)
    done_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    def done(self):
        self.done_at = timezone.now()
        return self.save()

    class Meta:
        db_table = "task"


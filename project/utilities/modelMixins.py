from django.db import models
import uuid

from rest_framework.pagination import PageNumberPagination


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


    def delete(self, *args, **kwargs):
        self.deleted = True
        return super(TimestampMixin, self).save()


class RequestMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = self.context.get("request")


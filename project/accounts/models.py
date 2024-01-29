import uuid

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.postgres.fields import ArrayField
from django.db import models



class RoleGroup(models.Model):
    group_name = models.CharField(max_length=36, blank=False, null=False)
    group_code = models.CharField(max_length=36, blank=False, null=False)
    group_permissions = ArrayField(models.CharField(
        blank=True,
        null=True, max_length=50
    ),
        size=100, default=list
    )

    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    """User model."""
    keycloak_uuid = models.CharField(max_length=36, blank=False, null=False)
    is_owner = models.BooleanField(default=False)

    user_roles = models.ForeignKey(RoleGroup, blank=True, null=True, on_delete=models.SET_NULL)
    neksio_roles = ArrayField(models.CharField(
        blank=True,
        null=True, max_length=50
    ),
        size=100, default=list
    )
    is_delete = models.BooleanField(default=False)
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    status = models.BooleanField(default=True)


    @property
    def is_manager(self):
        return "PERMISSIONS_CAN_LOGIN" in self.neksio_roles


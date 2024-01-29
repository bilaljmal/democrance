import uuid


from django.db import models
from utilities.modelMixins import TimestampMixin


class Customers(TimestampMixin):
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    dob = models.DateField(verbose_name="dob",blank=True, null=True)
    slug = models.SlugField(unique=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class InsurancePolicy(TimestampMixin):
    POLICY_TYPES = [
        ('personal', 'Personal'),('accident','Accident'),
    ]

    STATE_CHOICES = [
        ('new', 'New'),
        ('quoted', 'Quoted'),
        ('active', 'Active'),
        ('accepted', 'Accepted'),
    ]

    type = models.CharField(max_length=20, choices=POLICY_TYPES)
    premium = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    cover = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATE_CHOICES,default='quoted', blank=True)
    customer = models.ForeignKey(Customers,related_name="policies", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Type: {self.type} , Customer: {self.customer}"

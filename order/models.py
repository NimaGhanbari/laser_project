# Django
from django.db import models
from django_mysql.models import ListCharField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Python 
import random

User = get_user_model()


class Order(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID,_('void')),
        (STATUS_PAID,_('paid')),
        (STATUS_ERROR,_('error')),
        (STATUS_CANCELED,_('canceled')),
        (STATUS_REFUNDED,_('refunded'))
    )
    
    STATUS_TRANSLATIONS = {
        STATUS_VOID : _('payment could not be processed'),
        STATUS_PAID : _('payment succesfull'),
        STATUS_ERROR : _('payment has encontered an error . our technical team will check the'),
        STATUS_CANCELED : _('payment canceled by user.'),
        STATUS_REFUNDED :_('this payment has beed refunded')
    }
    
    STATUS_RECORD = 0
    STATUS_CONSTRUCTING = 10
    STATUS_MADE = 20
    STATUS_TRANSPORTATION = 30
    STATUS_CANCEL = 31
    STATUS_CHOICE = (
        (STATUS_RECORD,_('RECORD')),
        (STATUS_CONSTRUCTING,_('CONSTRUCTING')),
        (STATUS_MADE,_('MADE')),
        (STATUS_TRANSPORTATION,_('TRANSPORTATION')),
        (STATUS_CANCEL,_('CANCEL'))
    )
    ProductCodes = ListCharField(
        base_field=models.CharField(_("code"), max_length=7),
        size=15,
        max_length=130,  
    )
    ProductCounts = ListCharField(
        base_field=models.CharField(_("count"), max_length=4),
        size=15,
        max_length=90, 
    )
    Price = models.BigIntegerField()
    user = models.ForeignKey(to=User,related_name='Orders', on_delete=models.CASCADE)
    Address = models.TextField()
    status_pay = models.PositiveSmallIntegerField(verbose_name=_('pay status'),choices=STATUS_CHOICES,default=STATUS_VOID)
    status_build = models.PositiveSmallIntegerField(verbose_name=_('build status'),choices=STATUS_CHOICE,default=STATUS_RECORD)
    consumed_code = models.PositiveIntegerField(_("consumed refrence code"),null =True,db_index = True)
    create_time = models.DateTimeField(
        verbose_name=_("create time"), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_("update time"), auto_now=True)
    class Meta:
        db_table = "Orders"
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        
    def __str__(self):
        return str(self.user)
    

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    uid = models.AutoField (primary_key=True)
    tel = models.CharField(max_length=11, blank=False, null=False)
    pwd = models.CharField(max_length=10, blank=False, null=False)

class address(models.Model):
    aid = models.AutoField (primary_key=True)
    addr = models.CharField(max_length=100, blank=False, null=False)
    user = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
    )

class order(models.Model):
    oid = models.AutoField (primary_key=True)
    time = models.DateTimeField(auto_now=True,blank=False,null=False)
    price = models.FloatField(blank=False,null=False)
    status = models.CharField(max_length=30,blank=False,null=False)
    user = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
    )
    address = models.ForeignKey(
        'address',
        on_delete=models.CASCADE,
    )

class product(models.Model):
    pid = models.AutoField (primary_key=True)
    name = models.CharField(max_length=100,blank=False,null=False)
    price = models.FloatField(blank=False,null=False)
    num = models.IntegerField (blank=False,null=False)
    image_link = models.URLField(blank=False,null=False)
    second_category = models.ForeignKey(
        'second_category',
        on_delete=models.CASCADE,
    )

class chat(models.Model):
    oid = models.AutoField (primary_key=True)
    price = models.FloatField(blank=False,null=False)
    user = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
    )

class second_category(models.Model):
    scid = models.AutoField (primary_key=True)
    name = models.CharField(max_length=100,blank=False,null=False)
    first_category = models.ForeignKey(
        'first_category',
        on_delete=models.CASCADE,
    )

class first_category(models.Model):
    fcid = models.AutoField (primary_key=True)
    name = models.CharField(max_length=100,blank=False,null=False)

class order_product(models.Model):
    order = models.ForeignKey(
        'order',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        'product',
        on_delete=models.CASCADE,
    )
    pnum = models.IntegerField(blank=False,null=False)

class chat_pro(models.Model):
    chat = models.ForeignKey(
        'chat',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        'product',
        on_delete=models.CASCADE,
    )
    pnum = models.IntegerField(blank=False,null=False)

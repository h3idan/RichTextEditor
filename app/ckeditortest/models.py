#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2012-12-18 10:30
#**********************************


from django.db import models
from DjangoCkeditor.fields import RichTextField

class CkeditorTest(models.Model):

    title = models.CharField(verbose_name=u'标题', max_length=30)
    author = models.CharField(verbose_name=u'作者', max_length=30)
    details = RichTextField(verbose_name=u'内容')

    def __unicode__(self):
        return self.title



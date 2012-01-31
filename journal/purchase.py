# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models



class Purchase(models.Model):
	'''
	'''
	start_date = models.DateField(verbose_name=_(u'开始日期'))
	finished_date = models.DateField(verbose_name=_(u'完成日期'))
	buyer = models.ForeignKey(Employee,verbose_name=_(u'采购员'))

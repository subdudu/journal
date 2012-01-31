# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models



class Material(models.Model):
	'''库存物资
	'''
	code = models.CharField(verbose_name=_(u'物资编码'),max_length=32)
	name = models.CharField(verbose_name=_(u'正式品名'),max_length=192)
	short_name = models.CharField(verbose_name=_(u'品名简称'),max_length=48)
	manufacturer = models.ForeignKey(Manufacturer,verbose_name=_(u'生产商'))
	shelf_life = models.IntegerField(verbose_name=_(u'保质期（以天为单位）'))
	storage_condition = models.ForeignKey(StorageCondition,verbose_name=_(u'保存条件'))
	standard_price = models.IntegerField(verbose_name=_(u'标准价格'))
	standard_unit = models.CharField(verbose_name=_(u'标准计量单位'),max_length=16)
	standard_discount = models.ForeignKey(Discount,verbose_name=_(u'标准折扣'))



class Storage(models.Model):
	'''
	'''
	material_id = models.ForeignKey(Material,verbose_name=_(u'材料ID'))
	total_cost = models.FloatField(verbose_name=_(u'总成本'))
	amount = models.FloatField(verbose_name=_(u'数量'))
	warehouse = models.ForeignKey(Warehouse,verbose_name=_(u'存放仓库'))
	production_date = models.DateField(verbose_name=_(u'生产日期'))
	storaged_date = models.DateField(verbose_name=_(u'入库日期'))
	batch = models.ForeignKey(Purchase,verbose_name=_(u'采购批次'))

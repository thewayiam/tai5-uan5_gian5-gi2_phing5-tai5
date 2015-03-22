# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from 臺灣言語平臺.介面.加資料 import 加外語請教條
from 臺灣言語平臺.介面.加資料 import 加新詞影音
from 臺灣言語平臺.介面.加資料 import 加新詞文本
from 臺灣言語平臺.介面.資料列表 import 外語請教條列表

urlpatterns = patterns('',
	url(r'^加資料/外語請教條$', 加外語請教條, name='加外語請教條'),
	url(r'^加資料/新詞影音$', 加新詞影音, name='加新詞影音'),
	url(r'^加資料/新詞文本$', 加新詞文本, name='加新詞文本'),
	
	url(r'^外語請教條列表$', 外語請教條列表, name='外語請教條列表'),
	
)
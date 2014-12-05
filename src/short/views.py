# -*- coding: utf-8 -*-
#__author__='luffy@skyduy.com'
#__author__= 'http://www.skyduy.com'

import re, time, json
from func import addurl, getorigin
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def index(request):
    return render_to_response('index.html',{'info':''})#这里用到了csrf但实际上是没用到

def add(request):
    url = request.POST.get('url')
    url  = url[:100]
    try:
        ok, message = addurl(url)
    except Exception:
        ok = 0
        message = '系统繁忙...请稍后...'
    return HttpResponse(json.dumps({'ok' : ok, 'surl' : message}))

def jump(request,surl):
    ok,url = getorigin(surl)
    if(ok):
        return HttpResponseRedirect(url)
    else:
        return HttpResponse("该短链不存在.")

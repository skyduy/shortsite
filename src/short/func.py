#-*- coding: utf-8 -*-
import time, hashlib
import re
from sae.const import (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)

import MySQLdb, random, time

def getshort(time):
    code_map = (
           'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' ,
           'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' ,
           'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' ,
           'y' , 'z' , '0' , '1' , '2' , '3' , '4' , '5' ,
           '6' , '7' , '8' , '9'
            )
    hkeys = []
    s = time.encode('utf8') if isinstance(time, unicode) else time
    m = hashlib.md5()
    m.update(s)
    hex =  m.hexdigest()
    n = int(hex[3:11], 16)
    v = []
    e = 0
    for j in xrange(0, 3):
        x = 0x0000003D & n % 36#这里被我搞的不严谨了
        print x
        e |= ((0x00000002 & n ) >> 1) << j
        v.insert(0, code_map[x])
        n = n >> 6
    e |= n << 5
    v.insert(0, code_map[e & 0x0000003D])
    hkeys.append(''.join(v))
    return hkeys[0]

def putin(url,new):
    cxn = MySQLdb.connect(
        host  = MYSQL_HOST,
        port  = int(MYSQL_PORT),
        user  = MYSQL_USER,
        passwd = MYSQL_PASS,
        db = MYSQL_DB,
        charset = 'utf8')
    cur = cxn.cursor()
    try:
        cur.execute("INSERT INTO short_change (origin,new) VALUES(%s,%s)",(url,new))
    except Exception:
        cur.close()
        cxn.commit()
        return 0
    else:
        cur.close()
        cxn.commit()
        return 1

def addurl(url):
    rb = lambda x: x.replace(' ', '')
    url = rb(url).replace('\n','')
    n = re.match(r"\Ahttp://.*\..+\Z|\Ahttps://.*\..+\Z|\A.*\..+\Z",url.lower())
    if not n:
        return (0, '您输入的URL格式不正确，请确认后重新输入.')#0:格式错误
    if not re.match(r"\Ahttp.*",url.lower()):
            url='http://'+url
    TIME =url + str(time.time())

    surl = getshort(TIME)
    ok = putin(url,surl)
    return (ok,surl)

def getorigin(surl):
    cxn = MySQLdb.connect(
        host  = MYSQL_HOST,
        port  = int(MYSQL_PORT),
        user  = MYSQL_USER,
        passwd = MYSQL_PASS,
        db = MYSQL_DB,
        charset = 'utf8')
    cur = cxn.cursor()
    cur.execute("SELECT * FROM short_change WHERE new = %s",surl)
    all = cur.fetchall()
    cur.close()
    cxn.commit()
    try:
        url = all[0][1]
    except Exception:
        return (0,0)
    else:
        return (1,url)
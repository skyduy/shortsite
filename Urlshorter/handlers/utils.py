# coding: utf-8
import hashlib
import re
import time

__all__ = ['create_suffix', 'get_suffix']


def get_suffix(unique_str):
    code_map = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', '0', '1', '2', '3', '4', '5',
        '6', '7', '8', '9',
    )
    hkeys = []
    s = unique_str.encode('utf8') if isinstance(unique_str, unicode) else unique_str
    m = hashlib.md5()
    m.update(s)
    hex_str = m.hexdigest()
    n = int(hex_str[3:11], 16)
    v = []
    e = 0
    for j in xrange(0, 3):
        x = 0x0000003D & n % 36
        e |= ((0x00000002 & n) >> 1) << j
        v.insert(0, code_map[x])
        n >>= 6
    e |= n << 5
    v.insert(0, code_map[e & 0x0000003D])
    hkeys.append(''.join(v))
    return hkeys[0]


def add_to_db(url, new):
    from Urlshorter.models.url_record import Record
    try:
        question_answer = Record(url, new)
        question_answer.save()
    except Exception as e:
        print e
        return 0
    else:
        return 1


def create_suffix(url):
    rb = lambda x: x.replace(' ', '')
    url = rb(url).replace('\n', '')
    n = re.match(r"\Ahttp://.*\..+\Z|\Ahttps://.*\..+\Z|\A.*\..+\Z", url.lower())
    if not n:
        return 0, '您输入的URL格式不正确，请确认后重新输入.'
    if not re.match(r"\Ahttp.*", url.lower()):
            url = 'http://'+url
    unique_str = url + str(time.time())

    suffix = get_suffix(unique_str)
    ok = add_to_db(url, suffix)
    return ok, suffix


def get_origin(suffix):
    from Urlshorter.models.url_record import Record
    try:
        result = Record.query.filter_by(new=suffix)
        return 1, result.first().raw
    except Exception:
        return 0, 0

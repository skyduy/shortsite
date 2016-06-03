# coding: utf-8
import hashlib
import re
from Urlshorter.models.url_record import Record


def get_suffix(long_url):
    def get_md5(s):
        s = s.encode('utf8') if isinstance(s, unicode) else s
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()
    code_map = (
        '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 't', 'v',
        'w', 'x', 'y', 'z'
    )
    hkeys = []
    md5_str = get_md5(long_url)
    for i in xrange(0, 4):
        n = int(md5_str[i * 8:(i + 1) * 8], 16)
        v = []
        e = 0
        for j in xrange(0, 3):
            x = 0x00000023 & n
            e |= ((0x00000002 & n) >> 1) << j
            v.insert(0, code_map[x])
            n >>= 6
        e |= n << 5
        v.insert(0, code_map[e & 0x00000023])
        hkeys.append(''.join(v))
    return hkeys


def create_save_suffix(url):
    raw_url = url
    while True:
        suffixes = get_suffix(url)
        for suffix in suffixes:
            if Record.query.filter_by(new=suffix).first() is None:
                Record(raw_url, suffix).save()
                return 1, suffix
        url += '1'


def create_suffix(url):
    url = url.replace(' ', '').replace('\n', '')
    n = re.match(r"\Ahttp://.*\..+\Z|\Ahttps://.*\..+\Z|\A.*\..+\Z", url.lower())
    if not n:
        return 0, 'URL格式不正确，请重新输入.'
    if not re.match(r"\Ahttp.*", url.lower()):
            url = 'http://'+url

    result = Record.query.filter_by(raw=url).first()
    if result is not None:
        return 1, result.new
    else:
        ok, suffix = create_save_suffix(url)
        return ok, suffix


def get_origin(suffix):
    result = Record.query.filter_by(new=suffix).first()
    if result is not None:
        return 1, result.raw
    return 0, 0

# coding:utf-8
from __future__ import unicode_literals

import json
from flask import render_template, request, make_response, redirect, abort
from flask.views import MethodView
from Urlshorter.handlers.utils import create_suffix, get_origin


class Home(MethodView):
    def get(self):
        return render_template(
            'index.html',
            info='Make your lives easier',
        )

    def post(self):
        url = request.form['url']
        url = url[:190]
        ok, suffix = create_suffix(url)
        return make_response(json.dumps({'ok': ok, 'suffix': suffix}))


class Jump(MethodView):
    def get(self, suffix):
        ok, url = get_origin(suffix)
        if ok:
            return redirect(url)
        else:
            return abort(404)

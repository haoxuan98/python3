from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
import datetime
from django.shortcuts import render

def hello(request):
    return HttpResponse('Hello World')

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = 'now time is {}'.format(now)
#     return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = 'In {} hour(s),it will be {}.'.format(offset, dt)
    # return HttpResponse(html)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def current_datetime(request):
    now = datetime.datetime.now()
    d3 = now.strftime('%Y-%m-%d %H:%M:%S')
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date': d3})
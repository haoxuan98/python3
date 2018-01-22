from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
import datetime
from django.shortcuts import render, render_to_response
from .forms import ContactForm
from django.core.mail import send_mail
from books.models import User


def hello(request):
    return HttpResponse('Hello World')

def return_xml(request):
    return HttpResponse(open("templates/app.xml","rb"), content_type="text/xml")
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = 'now time is {}'.format(now)
#     return HttpResponse(html)

def get_time(request):
    return render(request, 'index.html')

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = 'In {} hour(s),it will be {}.'.format(offset, dt)
    # return HttpResponse(html)
    return render(
        request, 'hours_ahead.html', {
            'hour_offset': offset, 'next_time': dt})


def current_datetime(request):
    now = datetime.datetime.now()
    d3 = now.strftime('%Y-%m-%d %H:%M:%S')
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date': d3})

def login_do(request):
    data = {}
    name = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    try:
        b = User.objects.get(username=name)
        if b.password == password:
            data['result'] = True
            data['message'] = 'login success'
        else:
            data['result'] = False
            data['message'] = 'password wrong'
    except:
        data['result'] = False
        data['message'] = 'username not find'
    return JsonResponse(data)

def registe_do(request):
    data = {}
    name = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    try:
        User.objects.get(username=name)
        data['result'] = False
        data['message'] = 'The username has already existed'
    except:
        if len(name) != 0 and len(password) != 0:
            p1 = User(username=name, password=password)
            p1.save()
            data['result'] = True
            data['message'] = 'create user success'
        else:
            data['result'] = False
            data['message'] = "The username or password can not be empty"
    return JsonResponse(data)


def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')  # 重定向
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}  # 这里设定加载页面是填写在表单里面的初始值
        )
    return render(request, 'contact_form.html', {'form': form})

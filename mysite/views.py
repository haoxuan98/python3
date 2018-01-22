from django.shortcuts import render
from django.http import HttpResponse, Http404
from books.models import Book

# Create your views here.


def search_form(request):
    return render(request, 'search_form.html')


# def search(request):
#     if 'q' in request.GET:  # 这样可以避免因没有request.POST而抛出错误
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         books = Book.objects.filter(title__icontains=q)
#         return render(request, 'search_results.html',
#                       {'books': books, 'query': q})
#     else:
#         return render(request, 'search_form.html',
#                       {'error': True})

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                          {'books': books, 'query': q})
    return render(request, 'search_form.html',
                  {'errors': errors})

def my_time(request):
    return render(request, 'index.html')
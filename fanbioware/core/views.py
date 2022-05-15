from django.shortcuts import render


def page_not_found(request, exception):
    context = {
        'code': 404,
        'message': 'Oops, the page you’re looking for can’t be found.'
    }
    return render(
        request,
        'core/errors.html',
        context,
        status=404,
    )


def server_error(request):
    context = {
        'code': 500,
        'message': 'Internal server error. Try again after a while.'
    }
    return render(
        request,
        'core/errors.html',
        context,
        status=500,
    )

from django.shortcuts import render


def handler403(request, exception):
    """
    Render custom 403 page
    """
    return render(request, "errors/403.html", status=403)


def handler404(request, exception):
    """  Render custom 404 page"""
    return render(request, "errors/404.html", status=404)


def handler405(request, exception):
    """
    Render custom 405 page
    """
    return render(request, "errors/405.html", status=405)


def handler500(request):
    """
    Render custom 500 page
    """
    return render(request, "errors/500.html", status=500)

from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def main_page(request):
    return render(request, 'pet/main_page.html')

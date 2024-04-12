from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from pet.models import Pet


@require_http_methods(["GET"])
def main_page(request):
    pets = Pet.objects.all()
    return render(request, "pet/main_page.html", context={"pets": pets})

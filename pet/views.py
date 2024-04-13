from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from pet.models import Pet


@require_http_methods(["GET"])
def main_page(request):
    pets = Pet.objects.all()
    headlines = [
        {
            "title": "¡Haz un cambio hoy!",
            "description": "El indice de adopciones en Sucre subió un 6% en los últimos meses",
            "image_url":
                "https://gardenerspath.com/wp-content/uploads/2023/07/Labrador-Itching.jpg",
        },
        {
            "title": "Conoce a nuestros principales colaboradores",
            "description": "Vea el top de donadores del mes de abril del 2024",
            "image_url":
                "https://c1.peakpx.com/wallpaper/917/623/663/mammal-pet-cat-feline-wallpaper.jpg",
        },
        {
            "title": "Nuestros peludos luchadores se alistan para San Pedro",
            "description": "Nos preparamos para el evento más esperado por nuestros peludos",
            "image_url":
                "https://gardenerspath.com/wp-content/uploads/2023/07/Labrador-Itching.jpg",
        },
    ]
    return render(
        request, "pet/main_page.html", context={"pets": pets, "headlines": headlines}
    )

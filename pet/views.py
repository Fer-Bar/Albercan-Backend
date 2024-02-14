from django.shortcuts import render


def main_page(request):
    return render(request, 'pet/main_page.html')

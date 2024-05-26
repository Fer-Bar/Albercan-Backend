from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from people.models import Person


@method_decorator(require_http_methods(["GET"]), name='dispatch')
class PersonListView(ListView):
    queryset = Person.objects.filter(user__is_active=True)
    context_object_name = "people"
    template_name = "people/members.html"

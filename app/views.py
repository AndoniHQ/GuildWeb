from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Character

# Create your views here.


def index(request):
    return render(request, 'index.html', context={})


class CharacterListView(generic.ListView):
    model = Character
    template_name = "members.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the characters
        context['num_characters'] = Character.objects.all().count()
        context['character_list'] = Character.objects.all()
        return context

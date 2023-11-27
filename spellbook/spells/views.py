from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Spell

# Create your views here.
def index(request):
    spell_list = Spell.objects.all()

    #  TODO: change to hyperlink table view?
    output = ", ".join([s.name for s in spell_list])
    return HttpResponse(output)

def description(request, spell_id):
    spell_desc = Spell.objects.get(pk = spell_id)
    template = loader.get_template("spells/description.html")
    context = {
        "spell_desc": spell_desc,
    }
    return HttpResponse(template.render(context, request))



# maybe add spellbook account view
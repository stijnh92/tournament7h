from django.views.generic import ListView, DetailView
from tournament.models import Game
import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from django.shortcuts import get_object_or_404


class GameListView(ListView):
    model = Game
    template_name = 'public/game_list.html'


class GameDetailView(DetailView):
    model = Game
    template_name = 'public/game_detail.html'


def print_sheet(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    return render_to_pdf(
        'game_sheet.html',
        {
            'pagesize': 'A4',
            'game': game
        }
    )

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
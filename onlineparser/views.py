import os

from django.views.generic import DetailView, ListView, View
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from django.conf import settings

from forms import LogForm
from nexuiz_log_parser import NexuizLogParser, get_known_player_nicks
import utils

class ParserView(View):
    template_name = 'parsed_log.html'

    def get(self, request):
        form = LogForm()
        return render_to_response('parser.html', {'form': form}, context_instance=RequestContext(request))


    def post(self, request):
        form = LogForm(request.POST, request.FILES)
        if form.is_valid():
            filename = os.path.join(settings.MEDIA_ROOT, request.FILES['log'].name)
            utils.save_uploaded_file(filename, request.FILES['log'])
            nlp = NexuizLogParser(get_known_player_nicks('nexuiz_log_parser.players.PLAYERS'))
            nlp.parse_logs([filename.encode('ascii')])
            output = nlp.output(output='html')

            temp_template = os.path.join(settings.PROJECT_ROOT, 'onlineparser', 'templates', self.template_name)
            with open(temp_template, 'w') as dest:
                dest.write(output.decode('utf-8', 'ignore'))

            return render_to_response(self.template_name, {}, context_instance=RequestContext(request))


        return render_to_response('parser.html', {'form': form}, context_instance=RequestContext(request))
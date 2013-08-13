import os

from django.views.generic import DetailView, ListView, View
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from django.conf import settings

from forms import LogForm
import utils

class ParserView(View):

    def get(self, request):
        form = LogForm()
        return render_to_response('parser.html', {'form': form}, context_instance=RequestContext(request))


    def post(self, request):
        form = LogForm(request.POST, request.FILES)
        if form.is_valid():
            filename = os.path.join(settings.MEDIA_ROOT, request.FILES['log'].name)
            utils.save_uploaded_file(filename, request.FILES['log'])

        return render_to_response('parser.html', {'form': form}, context_instance=RequestContext(request))
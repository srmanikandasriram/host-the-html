from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext
from django.core.servers.basehttp import FileWrapper
import codecs,uuid,os

def upload(request):
  if request.method == "POST":
    html = request.POST.get('html','Nothing received!')
    while True:
      ufname = "media/" + str(uuid.uuid4())+'.html'
      if not os.path.isfile(ufname):
        break
    f = codecs.open(ufname,'w','utf-8')
    f.write(html)
    f.close()
#    f = open('templates/temporary.doc','r')
#    # generate the file
#    response = HttpResponse(FileWrapper(f), content_type='application/msword')
#    response['Content-Disposition'] = 'attachment; filename=export.doc'
#    return response
    return render_to_response('success.html', locals(), context_instance=RequestContext(request))
  else:
    #ufname = "#"
    #return render_to_response('success.html', locals(), context_instance=RequestContext(request))
    raise Http404()

def download(request):
  f = open('static/wiki-it-chrome.crx','r')
  response = HttpResponse(FileWrapper(f), content_type='application/x-chrome-extension')
  response['Content-Disposition'] = 'attachment; filename=wiki-it-chrome.crx'
  return response

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext
from django.core.servers.basehttp import FileWrapper
import codecs,uuid,os
import urllib2

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

def download(request,ufname):
  url = "http://pdfcrowd.com/url_to_pdf/"
  req = urllib2.Request(url)
  opener = urllib2.build_opener()
  req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36')
  req.add_header('Referer',"http://wiki-it-22162.apne1.actionbox.io:8080/"+ufname)
  response = opener.open(req)
  content = response.read()
  f = open(ufname[:-4]+"pdf","w")
  f.write(content)
  f.close()
  f = open(ufname[:-4]+"pdf","r")
  response = HttpResponse(FileWrapper(f), content_type='application/x-pdf')
  response['Content-Disposition'] = 'attachment; filename=wiki_it_download.pdf'
  return response

from django.shortcuts import render,reverse
from django.http import JsonResponse
from PublicSite import models
from UserAuthAPI import models as UserModels
# Static Files Path Reference
from CSSANet.settings import MEDIA_ROOT, MEDIA_URL
# CacheSettings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.views.decorators.cache import cache_page
# Create your views here.


############################### View Function ##########################################
# Set cache time for page
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def LoadPagetoRegister(uri,title,template):
    query_set = models.PageRegister.objects.filter(uri = uri)
    if not query_set:
        newRegister = models.PageRegister(
            uri = uri,
            title = title,
            templates = template
        )
        newRegister.save()
        print("New Registered")
    else:
        print("Page Already Registered "+title)



################################# View Controller ########################################
#@cache_page(CACHE_TTL)
def index(request):
    LoadPagetoRegister(reverse(index),'index','PublicSite/index.html')

    return render(request, 'PublicSite/index.html')
            
#@cache_page(CACHE_TTL)
def News(request):
    return render(request, 'PublicSite/News.html')

#@cache_page(CACHE_TTL)
def Departments(request,dept):
    ViewBag = {}
    ViewBag['MEDIA_ROOT'] = MEDIA_ROOT
    ViewBag['MEDIA_URL'] = MEDIA_URL
    LoadPagetoRegister(request.get_full_path(Departments),'Departments','PublicSite/dept.html')
    DeptInfo = UserModels.CSSADept.objects.filter(deptName=dept)
    if not DeptInfo:
        ViewBag['dept'] = None
    else:
        ViewBag['dept'] = DeptInfo[0]

    PageFields = models.HTMLFields.objects.filter(PageId__uri=request.get_full_path(Departments))

    for field in PageFields:
        if field.fieldType == 'text':
            ViewBag[field.fieldName.replace("-","")] = {'fieldInnerText':field.fieldInnerText}
        if field.fieldType == 'img':
            imgPath = models.ImgAttributes.objects.filter(RelatedField__id=field.id)[0].filePath
            ViewBag[field.fieldName.replace("-","")] = {
                'imgUri': imgPath.url
            }
    print(ViewBag)

    return render(request, 'PublicSite/dept.html', ViewBag)

#@cache_page(CACHE_TTL)
#def Events(requests):
#    return

################################# errors pages ########################################
from django.shortcuts import render
 
def bad_request(request):
 return render(request,'errors/page_400.html')

def permission_denied(request):
 return render(request,'errors/page_403.html')
 
def page_not_found(request):
 return render(request,'errors/page_404.html')
 
def server_error(request):
 return render(request,'errors/page_500.html')
################################# errors pages ########################################
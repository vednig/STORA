# import Http Response from django
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
# get datetime
import datetime

from matplotlib.pyplot import title

# create a function
def geeks_view(request):
	# fetch date and time
	now = datetime.datetime.now()
	# convert to string
	html = "Time is {}".format(now)
	# return response
	return HttpResponse(html)


from django.shortcuts import redirect

def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    else:
        return render(request, 'index.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json

@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })


def home(request):
	# fetch date and time
	now = datetime.datetime.now()
	# convert to string
	html = "Time is {}".format(now)
	# return response
	return render(request, 'index.html')
    #return render(request, 'index.html')


def dashboard(request):
	# fetch date and time
	now = datetime.datetime.now()
	# convert to string
	html = "Time is {}".format(now)
	logo={"src24":"https://cdn.statically.io/img/i.ibb.co/31sdg5s/icons8-box-60.png?h=24"}
	brand = {"title":"Branding","logo":logo}
	app = {"brand":brand}
	# return response
	return render(request, 'dashboard.html',{"app":app})



def static(request,title):
  returndict={}
  page="dashboard/"+title+".html"
  if title=="recent":
    returndict={"folderlist":[1,2,3]}
  return render(request, page,returndict)

def recent(request):
  recentlinks=["https://source.unsplash.com/520x300","https://source.unsplash.com/520x300?p","https://source.unsplash.com/520x300?n=1","https://source.unsplash.com/520x300?q=1"]
  html='''
          <div class="main">
            <!-- Add content here, remove div below -->
            <section class="overflow text-gray-700 ">
                <div class="container px-5 py-2 mx-auto lg:pt-12 lg:px-32">
                  <div class="flex flex-wrap -m-1 md:-m-2">
                    <div class="flex flex-wrap w-1/3 md:w-full md:flex-box">
                      <div class="w-full p-1 md:p-2">
                        <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg"
                          src="'''+recentlinks[0]+'''">
                      </div>
                    </div>
                    <div class="flex flex-wrap w-1/3">
                      <div class="w-full p-1 md:p-2">
                        <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg"
                          src="'''+recentlinks[1]+'''">
                      </div>
                    </div>
                    <div class="flex flex-wrap w-1/3">
                      <div class="w-full p-1 md:p-2">
                        <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg"
                          src="'''+recentlinks[2]+'''">
                      </div>
                    </div>
                    <div class="flex flex-wrap w-1/3">
                      <div class="w-full p-1 md:p-2">
                        <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg"
                          src="'''+recentlinks[3]+'''">
                      </div>
                    </div>
                   
                    
                  </div>
                </div>
              </section>
          </div>
        </div>

		 </script>
		 <script>
		 var Scrollbar = window.Scrollbar;
        var conScrollbar = document.getElementsByClassName('main')[0]
        Scrollbar.init(conScrollbar);
		</script>'''
  response = HttpResponse(html)
  return response

from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage

def upload(request):
    ## Save Path to id key
    if request.method == 'POST' and request.FILES['upload']:
        import pymongo
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)        
        client = pymongo.MongoClient("mongodb://user12:pass123@cluster0.hgojy.mongodb.net/streamdb?retryWrites=true&w=majority")
        db = client.streamdb
        people = db.people
        personDocument = {
  "profile": { "first": "Alan", "last": "Turing","email":"alanturing@email.com","image":"image.webp","lastIP":"<ip>","uid":"alan234","username":"turing2"},# UID Cannot Be Changed, User Name can be
  "paths": [ "/media/dict.png", "/media/file.jpg", "/doc/dist/dir/build.exe" ],
  "absolutePaths": { "/media/dict.png":"<cid>", "/media/file.jpg":"<cid>", "/doc/dist/dir/build.exe":"<cid>" },
  "bin":[],# Not to be listed
  "views": 1250000,
  "storageUsed":1000, # In MB
  "starred":[],
  "recent":[],
  "folders":[],
  "emptyFolder":[],
  "sharedWith":{"profile@email.com":"/path/to/folder","profile@email.com":"/path/to/file"},
  "recievedFrom":{"anotherperson@gmail.com":"path/to/his/folder"},
  "publicLinks":{"public":["share.megh.it/public/<key>/path/to/file"]},
  "privateLinks":{"private":["share.megh.it/private/<key>/path/to/file"]},
  "encryptedLinks":{"encrypted":{"share.megh.it/encryption/path/to/file":"password"}}


}
        people.insert_one(personDocument)
        db=client.test
        print(db)
        #print(file_url)
        return HttpResponse(str(file_url))
    return HttpResponse('No File Uploaded')
    
'''
def download(request):
    ## Use Key to find path then cid and access it via cdn infrastructure

def listfiles(request):
    ## list files in a particulat folder

def listfolders(request):
    ## list fsub-folders in a particular folder
    ## search similar keys

def modify(request):
    ## list files in a particulat folder


def delete(request):
    ## Deletes Record of It

def sendtobin(request):
  ## Adds Record to Bin
'''
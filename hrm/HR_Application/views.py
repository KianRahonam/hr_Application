from django.contrib.auth import authenticate, logout
from django.shortcuts import render

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, "main.html", {"username":user})
        else:
            return render(request, "index.html", {"message": "User / Password is Wrong"})

def logoutUser(request):
    logout(request)
    return render(request, "index.html")


def index(request):
    return render(request,"index.html")

def main(request):
    return render(request,"main.html")
# Create your views here.

def candidatedetials(request):
    return render(request,'candidatedetials.html')

def createofferpage(request):
    return render(request, 'createoffer.html')

def createoffer(request):
    from models import OfferLettercontract
    if request.method == 'POST':
        candidatename = request.POST['candidatename']
        offredcompany = request.POST['offredcompany']
        employmenttype = request.POST['employmenttype']
        offerdate = request.POST['offerdate']
        address = request.POST['address']
        location = request.POST['location']
        designation = request.POST['designation']
        salary = request.POST['salary']
        reporting = request.POST['reporting']
        joining = request.POST['joining']
        projectname = request.POST['projectname']
        contractend = ""
        phone = ""
        emialid = ""
        offerletter = OfferLettercontract(candidatename = candidatename,
                                          offredcompany = offredcompany,
                                          employmenttype = employmenttype,
                                          offerdate=offerdate,
                                          address=address,
                                          location=location,
                                          designation=designation,
                                          salary=salary,
                                          reporting=reporting,
                                          joining=joining,
                                          projectname=projectname,
                                          contractend=contractend,
                                          phone=phone,
                                          emialid=emialid)
        offerletter.save()
        data = offerletter.objects.all()
        return render(request, 'candidatedetials.html',{'data':data})
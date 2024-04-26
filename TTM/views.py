from django.shortcuts import render


def homePage(request):
    return render(request, "index.html")


def loginPage(request):
    return render(request, "login.html")


def contactPage(request):
    return render(request, "contactus.html")


def aboutPage(request):
    return render(request, "aboutus.html")


def registrationPage(request):
    return render(request, "register.html")

def insertpage(request):
    return render(request,"insert.html")

def updatepage(request):
    return render(request,"update.html")

def deletepage(request):
    return render(request,"delete.html")

def insertvehiclepage(request):
    return render(request,"insertvehicle.html")

def updatevehiclepage(request):
    return render(request,"updatevehicle.html")

def deletevehiclepage(request):
    return render(request,"deletevehicle.html")

def feedbackpage(request):
    return render(request,"feedback.html")

def paymentpage(request):
    return render(request,"payment.html")

def homepage(request):
    return render(request,"home.html")

def aboutpage(request):
    return render(request,"about.html")
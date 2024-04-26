from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle


class Register:
    pass


from .views import Register


def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            from TTM.adminapp.models import Register
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username existing ....")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing ...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd,)
                user.save()
                messages.info(request, "user created...")
                return render(request,"login.html")
        else:
            messages.info(request, "password is not matching....")
            return render(request,"register.html")
def checkinsert(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        if email==name:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "username existing...")
                return render(request, "login.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "Registration.html")
            else:
                user = Register.objects.create(name=name, email=email)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")

        return render(request, "Registration.html")
def checkupdate(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        if email==name:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "username existing...")
                return render(request, "login.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "index.html")
            else:
                user = Register.objects.create(name=name, email=email)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "Data updated Sucessfully...")
            return render(request, "index.html")

def checkdelete(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        if email==name:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "username existing...")
                return render(request, "login.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "index.html")
            else:
                user = Register.objects.create(name=name, email=email)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "Data updated Sucessfully...")
            return render(request, "deletevehicle.html")

def insertvehiclepage(request):
    return render(request,"insertvehicle.html")

def updatevehiclepage(request):
    return render(request,"updatevehicle.html")


def render(request, param):
    pass


def deletevehiclepage(request):
    return render(request,"deletevehicle.html")


class Vehicle:
    pass


def checkinsertvehicle(request):
    if request.method == "POST":
        make = request.POST["make"]
        model = request.POST["model"]
        year = request.POST["year"]
        price = request.POST["price"]
        image = request.FILES["image"]

        vehicle = Vehicle(make=make, model=model, year=year, price=price, image=image)
        vehicle.save()

        messages.info(request, "Vehicle added successfully!")
        return redirect("vehicle_list")
    else:
        return render(request, "insertvehicle.html")


class VehicleForm:
    pass


def checkupdatevehicle(request):
    if request.method == "POST":
        make = request.POST["make"]
        model = request.POST["model"]
        year = request.POST["year"]
        price = request.POST["price"]
        image = request.FILES["image"]

        vehicle = Vehicle(make=make, model=model, year=year, price=price, image=image)
        vehicle.save()

        messages.info(request, "Vehicle added successfully!")
        return redirect("vehicle_list")
        return HttpResponse('Thank you for your Updation!')
    else:
        return render(request, "updatevehicle.html")



def checkdeletevehicle(request):
    if request.method == "POST":
        id= request.POST["name"]
        if id == id:
            if Register.objects.filter(username=id).exists():
                messages.info(request, "Data deleted Successfully")
                return render(request, "insertvehicle.html")
            elif Register.objects.filter(id=id).exists():
                messages.info(request, "The details have been deleted")
                return render(request, "login.html")
            else:
                user = Register.objects.create(name=id)
                user.save()
                messages.info(request, "Data Deleted..")
                return render(request, "login.html")


        else:
            messages.info(request, "Delete the data carefully")
            return render(request, "login.html")


def checkfeedback(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        if email==name:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "Inserted Successfully..")
                return render(request, "feedback.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "feedback.html")
            else:
                user = Register.objects.create(name=name, email=email)
                user.save()
                messages.info(request, "user created...")
                feedback = request.POST.get('feedback')
                return HttpResponse('Thank you for your feedback!')
        else:
            messages.info(request, "Feedback uploaded Successfully...")
            return render(request, "feedback.html")
    return render(request, 'feedback.html')


def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwdd = request.POST["pwd"]
        flag = Register.objects.filter(username=name, password=pwdd).values()
        if flag: #flag isn't empty
            if name=="amruthavarshini": #amruthavarshini is admin
                messages.info(request,"This is Admin TTM Page")
                return render(request,"adminhome.html")

        if flag:
            messages.info(request,"This is User's TTM Page")
            return render(request, "ttmhome.html")
        else:
            messages.info(request, "Your credentials are not correct :(")
            return render(request, "loginfail.html")
def ttmhome(request):
    return render(request,"ttmhome.html")

class checkhome:
    def checkhome(request):
        return render(request,"home.html")


class checkabout:
    def checkabout(request):
        return render(request, "about.html")


def adminhome(request):
    return render(request,"adminhome.html")

class checkfeedback:
    def checkfeedback(request):
        return render(request, "feedback.html")

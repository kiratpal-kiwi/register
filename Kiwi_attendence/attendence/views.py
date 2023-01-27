from pyexpat.errors import messages

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from attendence.models import RegisterUser


# Create your views here.
def LoginPage(request):
    return render(request, 'login1.html')


def EmployeeAttendence(request):
    return render(request, "guard.html")


def Register(request):
    return render(request, "register.html")


def LoginUser(request):
    if request.method == "POST":
        emp_id = request.POST['emp_id']
        password = request.POST['pass']

        user = authenticate(Emp_id=emp_id, Password=password)

        if user is not None:
            login(request, user)
            return render(request, "admin.html")
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')


def AddUser(request):
    if request.method == "POST":

        f_name = request.POST['f_name']
        designation = request.POST['designation']
        email = request.POST['email']
        org = request.POST['org']
        pass1 = request.POST['psw']
        pass2 = request.POST['psw-repeat']
        department = request.POST['department']
        contact = request.POST['contact_number']

        if pass1==pass2:

            user = RegisterUser.objects.create(FullName=f_name,Designation=designation, Org=org, Password=pass1, ContactNumber=contact, Department=department, Email=email)
            user.Emp_id = "KTI-" + str(user.id)
            user.save()
            print(user.Emp_id)
            return redirect('login')
        else:
            return redirect('register')

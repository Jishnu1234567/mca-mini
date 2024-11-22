from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth,messages
from django.contrib.auth.models import User
from Prison_Management import urls
from django.urls import reverse
from.models import Visitor,Inmate,Report,Work
from django.contrib.auth.hashers import check_password  # To verify hashed passwords
from django.contrib.auth.decorators import login_required






def index(request):
    return render(request,"home.html")

def adminn_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        check = auth.authenticate(username=username, password=password)
        if check is not None:
            auth.login(request, check)
            return redirect('adminpage')
        else:
            msg = "Invalid Username Or Password"
            return render(request, "admin_login.html", {"msg": msg})
    else:
        return render(request, "admin_login.html")

def adminn(request):
    return render(request,"admin.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        check = auth.authenticate(username=username, password=password)
        if check is not None:
            auth.login(request, check)
            return redirect('indexpage')
        else:
            msg = "Invalid Username Or Password"
            return render(request, "user_login.html", {"msg": msg})
    else:
        return render(request,"user_login.html")

def user_signin(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        ucheck = User.objects.filter(username=username)
        echeck = User.objects.filter(email=email)
        if ucheck:
            msg = "Username Exits"
            return render(request, "user_signup.html", {"msg": msg})
        elif echeck:
            msg = "Email Exits"
            return render(request, "user_signup.html", {"msg": msg})
        elif password == "" or password != repassword:
            msg = "Invalid Password"
            return render(request, "user_signup.html", {"msg": msg})
        else:
            user = User.objects.create_user(
                first_name=name, username=username, email=email, password=password)
            user.save()
            return render(request,"home.html")
    else: 
        return render(request,"user_signup.html")

def guard_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        check = auth.authenticate(username=username, password=password)
        if check is not None:
            auth.login(request, check)
            return redirect("gaurds_home_page")
        else:
            msg = "Invalid Username Or Password"
            return render(request, "guard_login.html", {"msg": msg})
    else:
        return render(request,"guard_login.html")
    

def guard_signin(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        ucheck = User.objects.filter(username=username)
        echeck = User.objects.filter(email=email)
        if ucheck:
            msg = "Username Exits"
            return render(request, "guard_signup.html", {"msg": msg})
        elif echeck:
            msg = "Email Exits"
            return render(request, "guard_signup.html", {"msg": msg})
        elif password == "" or password != repassword:
            msg = "Invalid Password"
            return render(request, "guard_signup.html", {"msg": msg})
        else:
            user = User.objects.create_user(
                first_name=name, username=username, email=email, password=password)
            user.save()
            return render(request,"gaurds_home.html")
    else: 
        return render(request,"guard_signup.html")

def visitors_request(request):
    name = request.GET.get("name")
    username = request.GET.get("user")
    return render(request,"visitors_request.html",{"name":name,"username":username})

def visitors_history(request):
    if request.method == "POST":
        name = request.POST.get("username")
        ivisitor = request.POST.get("ivisitor")
        email = request.POST.get("email")
        iname = request.POST.get("iname")
        relationship = request.POST.get("relationship")
        visitdate = request.POST.get("visitdate")
        visittime = request.POST.get("visittime")
        purpose = request.POST.get("purpose")
        visitor = Visitor.objects.create(
            name=name,
            aadhar=ivisitor,
            email=email,
            inmate_name=iname,
            relationship=relationship,
            date=visitdate,
            time=visittime,
            purpose=purpose
        )
        history=Visitor.objects.filter(name=name)
       
        return render(request,"visit_history.html",{"history":history})
    else:
        name = request.GET.get("name")
        history=Visitor.objects.filter(name=name)
        return render(request,"visit_history.html",{"history":history})

def logout(request):
    auth.logout(request)
    return render(request,"home.html")

def inmate_list(request):
    inmates=Inmate.objects.all()
    return render(request,"inmate_full.html",{"inmates":inmates})

def single_inmate(request):
    id = request.GET.get("id")
    inmate=Inmate.objects.filter(id=id)
    return render(request,"single_inmates.html",{"inmate":inmate})

def gaurds_home(request):
    return render(request,"gaurds_home.html")

@login_required
def report_page(request):
    inmates = Inmate.objects.all()
    if request.method == "POST":
        value = request.POST.get("inmate-name")
        name, pro = value.split(',')
        id=Inmate.objects.get(id=pro)
        desc = request.POST.get("desc")
        date = request.POST.get("date")
        reported_by = request.POST.get("gaurd_name")
        print(date)
        print(reported_by)
        record = Report.objects.create(pro=id, name=name, desc=desc, date=date,reported_by=reported_by)
        record.save()
        report=Report.objects.all()
        return render(request, "violent_activity_report.html", {"inmates": inmates, "name": name, "desc": desc, "date": date, "record": record,"report": report,"User": request.user})
    else:
        # Render the page for GET requests without processing a form submission
        report=Report.objects.all()
        return render(request, "violent_activity_report.html", {"inmates": inmates,"report": report})
    
def delete_report(request):
    # Use square brackets instead of parentheses to get the 'id' parameter
    report_id = request.GET["id"]
    report = get_object_or_404(Report, id=report_id)
    report.delete()  # Delete the report from the database
    return redirect('report_page')  # Redirect to the report page by its URL name

@login_required
def assign_work(request):
    inmates = Inmate.objects.all()
    work_choices = Work.STATUS_CHOICES  # Access the choices from the Work model
    work = Work.objects.all()  # Get all assigned work
    if request.method == "POST":
        inmate_id = request.POST.get("inmate-name")
        work_type = request.POST.get("work-type")
        work_date = request.POST.get("date")
        inmate = Inmate.objects.get(id=inmate_id)
        reported_by = request.POST.get("gaurd_name")
        Work.objects.create(pro=inmate, work=work_type, date=work_date,reported_by=reported_by)
        return redirect('assign_work_page')
    return render(request, "work_assign_inmate.html", {"inmates": inmates, "work_choices": work_choices, "work": work,"User": request.user})

def delete_work(request):
    work_id = request.GET.get("id")
    work = get_object_or_404(Work, id=work_id)
    work.delete()
    return redirect('assign_work_page')  


def guard_inmate_list(request):
    inmates=Inmate.objects.all()
    return render(request,"guard_inmate_full.html",{"inmates":inmates})

def admin_inmate_list(request):
    inmates=Inmate.objects.all()
    return render(request,"admin_inmate_full.html",{"inmates":inmates})

def guard_single_inmate(request):
    id = request.GET.get("id")
    inmate=Inmate.objects.filter(id=id)
    return render(request,"guard_single_inmate.html",{"inmate":inmate})
def admin_single_inmate(request):
    id = request.GET.get("id")
    inmate=Inmate.objects.filter(id=id)
    return render(request,"admin_single_inmate.html",{"inmate":inmate})



def admin_guard_register(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        ucheck = User.objects.filter(username=username)
        echeck = User.objects.filter(email=email)
        if ucheck:
            msg = "Username Exits"
            return render(request, "admin_guard_register.html", {"msg": msg})
        elif echeck:
            msg = "Email Exits"
            return render(request, "admin_guard_register.html", {"msg": msg})
        elif password == "" or password != repassword:
            msg = "Invalid Password"
            return render(request, "admin_guard_register.html", {"msg": msg})
        else:
            user = User.objects.create_user(
                first_name=name, username=username, email=email, password=password)
            user.save()
            msg = "Account Created"
            return render(request,"admin_guard_register.html", {"msg": msg})
    else: 
        return render(request,"admin_guard_register.html")
    


def admin_visit_history(request):
    if request.method == "POST":
        visitor_id = request.POST.get("visitor_id")
        action = request.POST.get("action")
        admin_message = request.POST.get("admin_message", "")
        visitor = get_object_or_404(Visitor, id=visitor_id)

        if action == "accept":
            visitor.status = "ACCEPTED"
            messages.success(request, "Appointment accepted.")
        elif action == "reject":
            visitor.status = "REJECTED"
            messages.success(request, "Appointment rejected.")

        visitor.admin_message = admin_message  # Save admin's message
        visitor.save()
        return redirect("admin_visit_history_page")

    history = Visitor.objects.all()
    return render(request, "admin_visitors_request.html", {"history": history})



def admin_inmate_report(request):
    report=Report.objects.all()
    return render(request,'admin_inmate_reports.html',{"report":report})


def admin_inmate_delete_report(request):
    report_id = request.GET["id"]
    report = get_object_or_404(Report, id=report_id)
    report.delete()  
    report=Report.objects.all()
    return render(request,'admin_inmate_reports.html',{"report":report})

def admin_inmate_work(request):
    work=Work.objects.all()
    return render(request,'admin_inmate_work_page.html',{"work":work})


def admin_inmate_delete_work(request):
    work_id = request.GET["id"]
    work = get_object_or_404(Work, id=work_id)
    work.delete()  
    work=Work.objects.all()
    return render(request,'admin_inmate_work_page.html',{"work":work})



def main(request):
    return render(request,"index.html")


def admin_add_inmate(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        crime = request.POST.get("crime")
        sentence = request.POST.get("sentence")
        entry_date = request.POST.get("entry_date")
        release_date = request.POST.get("release_date")
        img=request.FILES.get('photo')
        inmate=Inmate.objects.create(name=name,age=age,crime=crime,sentence=sentence,entry_date=entry_date,exit_date=release_date,img=img)
        inmate.save()
        return render(request,"admin_add_inmate.html")

    else:
        return render(request,"admin_add_inmate.html")





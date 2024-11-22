"""
URL configuration for Prison_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path( "",views.main,name="mainpage"),
    path( "index/",views.index,name="indexpage"),
    path( "adminn/",views.adminn_login,name="adminloginpage"),
    path( "adminnpage/",views.adminn,name="adminpage"),
    path( "userlogin/",views.user_login,name="userloginpage"),
    path( "usersignin/",views.user_signin,name="usersigninpage"),
    path( "guardlogin/",views.guard_login,name="guardloginpage"),
    path( "guardsignin/",views.guard_signin,name="guardsigninpage"),
    path( "visitors_request/",views.visitors_request,name="visitors_request_page"),
    path( "visitors_history/",views.visitors_history,name="visitors_history_page"),
    path("logout/",views.logout,name="logoutpage"),
    path("inmate_list/",views.inmate_list,name="inmate_list_page"),
    path("single_inmate/",views.single_inmate,name="single_inmate_page"),
    path("gaurds_home/",views.gaurds_home,name="gaurds_home_page"),
    path("report_page/",views.report_page,name="report_page"),
    path("delete_report/",views.delete_report,name="delete_report_page"),
    path("assign_work/",views.assign_work,name="assign_work_page"),
    path("delete_work/",views.delete_work,name="delete_work_page"),
    path("guard_single_inmate/",views.guard_single_inmate,name="guard_single_inmate_page"),
    path("admin_single_inmate/",views.admin_single_inmate,name="admin_single_inmate_page"),
    path("guard_inmate_list/",views.guard_inmate_list,name="guard_inmate_list_page"),
    path("admin_inmate_list/",views.admin_inmate_list,name="admin_inmate_list_page"),
    path("admin_guard_register/",views.admin_guard_register,name="admin_guard_register_page"),
    path("admin_visit_history/",views.admin_visit_history,name="admin_visit_history_page"),
    path("admin_inmate_report/",views.admin_inmate_report,name="admin_inmate_report_page"),
    path("admin_inmate_delete_report/",views.admin_inmate_delete_report,name="admin_inmate_delete_report_page"),
    path("admin_inmate_work/",views.admin_inmate_work,name="admin_inmate_work_page"),
    path("admin_inmate_delete_work/",views.admin_inmate_delete_work,name="admin_inmate_delete_work_page"),
    path("admin_add_inmate/",views.admin_add_inmate,name="admin_add_inmate_page"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

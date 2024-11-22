from django.contrib import admin
from .models import Visitor,Inmate,Report,Work



class VisitorAdmin(admin.ModelAdmin):
    list_display = ("name","aadhar","email","inmate_name","relationship","date","time","purpose","status")


class InmateAdmin(admin.ModelAdmin):
    list_display = ("name","age","crime","sentence","entry_date","exit_date","img")

class ReportAdmin(admin.ModelAdmin):
    list_display = ("pro","name","desc","date","reported_by")

class WorkAdmin(admin.ModelAdmin):
    list_display = ("pro","work","date")




admin.site.register(Visitor,VisitorAdmin)
admin.site.register(Inmate,InmateAdmin)
admin.site.register(Report,ReportAdmin ) 
admin.site.register(Work,WorkAdmin)

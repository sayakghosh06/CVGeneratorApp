from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
from django.contrib import messages
# Create your views here.

def index(request):

    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        summary=request.POST['summary']
        degree=request.POST['degree']
        school=request.POST['school']
        university=request.POST['university']
        previous_work=request.POST['previous_work']
        skills=request.POST['skills']
        trainings_courses=request.POST['trainings_courses']
        achievements=request.POST['achievements']
        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills,trainings_courses=trainings_courses,achievements=achievements)

        profile.save()

        messages.success(request,"You Have Created Your CV Successfully")

    return render(request,'index.html')


def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('resume.html')
    html = template.render({'user_profile':user_profile})
    options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename = "resume.pdf"
    return response


def list(request):
    user_profiles= Profile.objects.all()
    context= {'user_profiles':user_profiles}
    return render(request,'list.html',context)

   





   

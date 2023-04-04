from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Questions

def questions(request):
    myquestions = Questions.objects.all()
   
    context = {
        'myquestions' : myquestions,
    }
    return render( request,'all_questions.html',context)


def details(request, id):
  myquestions = Questions.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
     'myquestions' : myquestions ,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# Create your views here.

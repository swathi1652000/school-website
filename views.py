from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def aboutus(request):
	return render(request,'aboutus.html')
def Maharishi_Vidya_Mandir(request):
	return render(request,'Maharishi_Vidya_Mandir.html')
def contactus(request):
	return render(request,'contactus.html')
def busses(request):
	return render(request,'busses.html')
def bhavans(request):
	return render(request,'bhavans.html')
def ac(request):
	return render(request,'ac.html')
def ac2(request):
	return render(request,'ac2.html')
def activities(request):
	return render(request,'activities.html')
def admission(request):
	return render(request,'admission.html')
def Admissionform(request):
	return render(request,'Admissionform.html')
def busses(request):
	return render(request,'busses.html')
def CCA(request):
	return render(request,'CCA.html')
def cca2(request):
	return render(request,'cca2.html')
def Classrooms(request):
	return render(request,'Classrooms.html')
def dicom(request):
	return render(request,'dicom.html')
def educomp(request):
	return render(request,'educomp.html')
def f1(request):
	return render(request,'f1.html')
def form1(request):
	return render(request,'form1.html')
def forms(request):
	return render(request,'forms.html')
def hostel(request):
	return render(request,'hostel.html')
def imagemap(request):
	return render(request,'imagemap.html')
def labs(request):
	return render(request,'labs.html')
def library(request):
	return render(request,'library.html')
def ncc(request):
	return render(request,'ncc.html')
def osla(request):
	return render(request,'osla.html')
def playgrounds(request):
	return render(request,'playgrounds.html')
def RESULTS(request):
	return render(request,'RESULTS.html')
def rulesandregulations(request):
	return render(request,'rulesandregulations.html')
def sports(request):
	return render(request,'sports.html')
def XSEED(request):
	return render(request,'XSEED.html')
def photogallery(request):
	return render(request,'photogallery.html')
def specialfeatures(request):
	return render(request,'specialfeatures.html')
def infrastructure(request):
	return render(request,'infrastructure.html')
def admission(request):
	return render(request,'admission.html')
def results(request):
	return render(request,'results.html')
def cocurricularactivities(request):
	return render(request,'cocurricularactivities.html')
def orgchart(request):
	return render(request,'orgchart.html')
def form5(request):
	return render(request,'form5.html')
def Highform(request):
	return render(request,'Highform.html')
def Educomp(request):
	return render(request,'educomp.html')












'''
def showform(request):
    form= BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'tvreview.html', context)
'''
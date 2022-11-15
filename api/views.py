from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


# Create your views here.
@api_view(['GET'])
def home(request):
    students = Student.objects.all()
    studentsserializer = Studentserializer(students, many=True)
    return Response(studentsserializer.data)

@api_view(['GET'])    
def studentlist(request,pk):
    student= Student.objects.get(id=pk)
    studentserializer=Studentserializer(student,many=False)
    return Response(studentserializer.data)

@api_view(['POST'])
def addstudent(request):
    serialdata=Studentserializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()
    return Response(serialdata.data)    

@api_view(['POST'])
def updatestudent(request,pk):
    student=Student.objects.get(id=pk)
    serialstudent=Studentserializer(instance=student, data=request.data)
    if serialstudent.is_valid():
        serialstudent.save()
    return Response(serialstudent.data)    

@api_view(['DELETE'])
def deletestudent(request, pk):
    student=Student.objects.get(id=pk)
    student.delete()

    students = Student.objects.all()
    studentsserializer = Studentserializer(students, many=True)
    return Response(studentsserializer.data)
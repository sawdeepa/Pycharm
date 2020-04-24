from django.shortcuts import render
from .models import TableM
import numpy as np
from django.http import JsonResponse
from django.db import connection, transaction
from django.http import HttpResponse
from rest_framework import viewsets
import pyodbc
from datetime import date
# Create your views here.
def submit2(request):
    Qry2 = request.GET["SQL"]
    print(Qry2)
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.118.23.78;"
                          "Database=D-DASH_Phase0_DQ;"
                          "UID=dsuser;"
                          "PWD=Password.1;"
                          # "Trusted_Connection=yes;"
                          )
    cursor = conn.cursor()
    Qry=[]

    cursor.execute(Qry2)
    names = list(map(lambda x: x[0], cursor.description))
    Qry.append(names)

    for row in cursor.fetchall():
        l =[]
        for i in range(0,len(row)):
            l.append(row[i])
        Qry.append(l)

    conn.close()
    return render(request, 'DEMOAPP1/result.html', {'Query': Qry})

def submit(request):
    Qry2 = request.GET["SQL"]
    print(Qry2)
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.118.23.78;"
                          "Database=D-DASH_Phase0_DQ;"
                          "UID=dsuser;"
                          "PWD=Password.1;"
                          # "Trusted_Connection=yes;"
                          )
    cursor = conn.cursor()
    Qry=[]

    cursor.execute(Qry2)
    names = list(map(lambda x: x[0], cursor.description))
    Qry.append(names)

    for row in cursor.fetchall():
        l =[]
        for i in range(0,len(row)):
            l.append(row[i])
        Qry.append(l)

    conn.close()
    return render(request, 'DEMOAPP1/result.html', {'Query': Qry})
    #return render(request, 'DEMOAPP1/result.html',{'Query':Qry},{'Family1':dest})

def insi(request):
    T_list=TableM.objects.order_by('id')
    T_dict = {'access_records': T_list}
    return render(request, 'DEMOAPP1/resultinsight.html', context=T_dict)

def details(request, id):

    print('str',id)

    Qry21 =TableM.objects.filter(pk=id).values('Query')
    for data in Qry21:
       Q1=data['Query']
    print(Q1)
    Qry22 = Q1
    print(Qry22)
    Qry22rr= 'Select count(*) from (' + Qry22 + ')'
    print(Qry22rr)
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.118.23.78;"
                          "Database=D-DASH_Phase0_DQ;"
                          "UID=dsuser;"
                          "PWD=Password.1;"
                          # "Trusted_Connection=yes;"
                          )
    cursor = conn.cursor()
    Qry1111 = []

    cursor.execute(Qry22)

    names = list(map(lambda x: x[0], cursor.description))
    Qry1111.append(names)
    a = 1
    for row in cursor.fetchall():
        l = []

        for i in range(0, len(row)):
            l.append(row[i])
        a=a+1
        Qry1111.append(l)
    print(a)

    TableM.objects.filter(pk=id).update(Recordcount=a)
    TableM.objects.filter(pk=id).update(LastRefreshedOn=date.today())
    L_list = TableM.objects.filter(pk=id).values('Recordcount')
    print(L_list)
    conn.close()
    return render(request, 'DEMOAPP1/result.html', {'Query': Qry1111})


def refresh(request,id):

    print('str', id)

    Qry21 = TableM.objects.filter(pk=id).values('Query')
    for data in Qry21:
        Q1 = data['Query']
    print(Q1)
    Qry22 = Q1
    print(Qry22)

    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.118.23.78;"
                          "Database=D-DASH_Phase0_DQ;"
                          "UID=dsuser;"
                          "PWD=Password.1;"
                          # "Trusted_Connection=yes;"
                          )
    cursor = conn.cursor()
    Qry1111 = []

    cursor.execute(Qry22)

    names = list(map(lambda x: x[0], cursor.description))
    Qry1111.append(names)
    a = 1
    for row in cursor.fetchall():
        l = []

        for i in range(0, len(row)):
            l.append(row[i])
        a = a + 1
        Qry1111.append(l)
    print(a-1)
    TableM.objects.filter(pk=id).update(Recordcount=a-1)
    TableM.objects.filter(pk=id).update(LastRefreshedOn=date.today())
    L_list = TableM.objects.filter(pk=id).values('Recordcount')
    print(L_list)
    T_list=TableM.objects.order_by('id')
    T_dict = {'access_records': T_list}
    return render(request, 'DEMOAPP1/resultinsight.html', context=T_dict)


def graphs(request,id):
        QryTableM = TableM.objects.filter(pk=id).values('Query')
        for data in QryTableM:
            Q1 = data['Query']
        QryTableM = TableM.objects.filter(pk=id).values('Insight')
        for data in QryTableM:
            QInsight = data['Insight']
        Insight=QInsight
        Qry22 = Q1
        print(Qry22)
        conn = pyodbc.connect("Driver={SQL Server};"
                              "Server=10.118.23.78;"
                              "Database=D-DASH_Phase0_DQ;"
                              "UID=dsuser;"
                              "PWD=Password.1;"
                              # "Trusted_Connection=yes;"
                              )
        cursor = conn.cursor()
        Qry = []

        cursor.execute(Qry22)
        names = list(map(lambda x: x[0], cursor.description))
        Qry.append(names)

        for row in cursor.fetchall():
            l = []
            for i in range(0, len(row)):
                l.append(row[i])
            Qry.append(l)
        print(Qry)
        Qryarr=np.array(Qry)
        print(type(Qryarr))
        conn.close()
        a ='Graph'+str(id)+'.html';
        return render(request,'DEMOAPP1/'+a, {'Query': Qry,'Insight':Insight})
        #return render(request, 'DEMOAPP1/Graph.html', {'QueryInsight': QryInsight})


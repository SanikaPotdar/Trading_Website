from django.shortcuts import render
from joblib import load
import matplotlib.pyplot as plt
import io
import urllib, base64
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from django.http import JsonResponse
import requests

xnew = load('./savedModules/xnew.joblib')
x = [xnew[0], xnew[1], xnew[2]]

# Create your views here.
def main(request):
    plt.figure(figsize=(5, 5))
    emotions_list = ['Neutral','Negative','Positive']
    colors = ['plum', 'pink', 'peachpuff','paleturquoise','thistle','lightsteelblue']
    plt.pie(x, colors=colors, labels=emotions_list, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    plt.legend()
    plt.title("Outcome")
    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    # print("vallllllllllllllllllllll",xnew[2])
    # labels = 'Sale', 'Purchase', 'bas'
    # print("vxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",labels)
    # # sizes = [random.randint(10,30), random.randint(30,50)]
    # # explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    # fig1, ax1 = plt.subplots()
    # ax1.pie(x, labels=labels, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # plt.savefig('/savedModules/sale_purchase_peichart.png',dpi=100)
    return render(request, 'index.html', {'data':uri})

def charts(request):
    return render(request, 'charts.html')

# def senti(request):
#     plt.figure(figsize=(5, 5))
#     emotions_list = ['Neutral','Negative','Positive']
#     colors = ['plum', 'pink', 'peachpuff','paleturquoise','thistle','lightsteelblue']
#     plt.pie(x, colors=colors, labels=emotions_list, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
#     plt.legend()
#     plt.title("Outcome")
#     fig = plt.gcf()
#     #convert graph into dtring buffer and then we convert 64 bit code into image
#     buf = io.BytesIO()
#     fig.savefig(buf,format='png')
#     buf.seek(0)
#     string = base64.b64encode(buf.read())
#     uri =  urllib.parse.quote(string)
#     return render(request, 'index.html',{'data':uri})

def indian(request):
    return render(request, 'investing_chart.html')

# def login(request):
#     return render(request, 'signup.html')

# def signup(request):
#     return render(request, 'signup.html')

def login1(request):
    return render(request, 'login.html')

# def back(request):
#     return render(request, 'index.html')

def tables(request):
    return render(request, 'tables.html')

# def signout(request):
#     return render(request, 'signout.html')

def crypto(request):
    return render(request, 'grid.html')

def form(request):
    return render(request, 'form-common.html')

def market(request):
    return render(request, 'form-validation.html')


def news(request):
    r = requests.get('https://newsapi.org/v2/everything?q=TCS&sortBy=publishedAt&apiKey=b4f79812d6f44ce6b4d6775af9d81dde')
    return JsonResponse(r.json())



    
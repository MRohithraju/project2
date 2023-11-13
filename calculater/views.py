from django.shortcuts import render
from django.http import HttpResponse

# Create yourviews here.
def input(request):
    return render(request,"input.html")

def calculate(request):
    try:
        v1=request.GET["t1"]
        v2=request.GET["t2"]
        operation_type=request.GET["op"]
        i=int(v1)
        j=int(v2)
        if operation_type=="add":
            k=i+j
            return HttpResponse("<htmL><body bg color=orange><h1> the sum is:"+str(k)+"</h1></body></html>")
        if operation_type=="sub":
            k=i-j
            return HttpResponse("<htmL><body bg color=green><h1> the sum is:"+str(k)+"</h1></body></html>")
        if operation_type=="mul":
            k=i*j
            return HttpResponse("<htmL><body bg color=pink><h1> the sum is:"+str(k)+"</h1></body></html>")
        else:
            k=i/j
            return HttpResponse("<htmL><body bg color=lightblue><h1> the sum is:"+str(k)+"</h1></body></html>")

    except(ValueError):
        return HttpResponse("invalid data")



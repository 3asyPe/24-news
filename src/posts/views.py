from django.shortcuts import render


# РАЗБЕРИ
def hello(request, *args, **kwargs):
    return render(request, "base.html", {})

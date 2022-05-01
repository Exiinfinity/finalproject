from django.shortcuts import render
def home(request):
    context={
    }
    return render(request, 'main.html', context)

def register(request):
    context={
    }
    return render(request, 'register.html', context)

def main(request):
    context={
    }
    return render(request, 'main.html', context)

def plantinfo(request):
    context={
    }
    return render(request, 'plantinfo.html', context)

def plantmanage(request):
    context={
    }
    return render(request, 'plantmanage.html', context)

def plantrecog(request):
    context={
    }
    return render(request, 'plantrecog.html', context)

def plantdisease(request):
    context={
    }
    return render(request, 'plantdisease.html', context)

def plantrecog(request):
    context={
    }
    return render(request, 'plantrecog.html', context)

def search(request):
    context={
    }
    return render(request, 'search.html', context)



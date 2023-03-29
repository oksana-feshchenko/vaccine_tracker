from django.shortcuts import render

from tracker.models import Child, Parent


def index(request):
    num_children = Child.objects.count()
    num_parents = Parent.objects.count()

    context = {
        "num_children": num_children,
        "num_parents": num_parents,
    }

    return render(request, "tracker/index.html", context=context)

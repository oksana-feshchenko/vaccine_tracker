from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tracker.models import Child, Parent, Vaccine, Vaccination


def index(request):
    num_children = Child.objects.count()
    num_parents = Parent.objects.count()

    context = {
        "num_children": num_children,
        "num_parents": num_parents,
    }

    return render(request, "tracker/index.html", context=context)


class VaccineListView(generic.ListView):
    model = Vaccine
    queryset = Vaccine.objects.all()
    template_name = "tracker/vaccine_list.html"


class ChildListView(generic.ListView):
    model = Child
    queryset = Child.objects.prefetch_related("vaccinations__vaccine")
    template_name = "tracker/child_list.html"


class ChildDetailView(generic.DetailView):
    model = Child
    queryset = Child.objects.prefetch_related("vaccinations")
    template_name = "tracker/child_detail.html"


class ChildCreateView(generic.CreateView):
    model = Child
    fields = "__all__"
    success_url = reverse_lazy("tracker:child-list")


class ChildUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Child
    fields = "__all__"
    success_url = reverse_lazy("tracker:child-list")


class ChildDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Child
    success_url = reverse_lazy("tracker:child-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context


class VaccinationDetailView(generic.DetailView):
    model = Vaccination
    queryset = Vaccination.objects.prefetch_related("complications")
    template_name = "tracker/vaccination_detail.html"





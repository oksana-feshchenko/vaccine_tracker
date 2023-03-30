from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from tracker.forms import VaccinationCreateForm, ComplicationCreateForm
from tracker.models import Child, Parent, Vaccine, Vaccination, Complication


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context


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
    template_name = "tracker/vaccination_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context


class VaccinationCreateView(generic.CreateView):
    model = Vaccination
    form_class = VaccinationCreateForm

    def get(self, request, *args, **kwargs):
        child_id = self.kwargs.get('pk')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        child = get_object_or_404(Child, pk=self.kwargs['pk'])
        form.instance.child = child
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context

    def get_success_url(self, **kwargs):
        return reverse("tracker:child-detail", kwargs={'pk': self.kwargs['pk']})


class VaccinationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Vaccination
    fields = ("vaccine", )

    def get_success_url(self, **kwargs):
        return reverse("tracker:vaccination-detail", kwargs={'pk': self.kwargs['pk']})


class VaccinationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Vaccination

    def get_success_url(self, **kwargs):
        return reverse("tracker:child-detail", kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context

class ComplicationListView(generic.ListView):
    model = Complication
    template_name = "tracker/complication_list.html"


class ComplicationCreateView(generic.CreateView):
    model = Complication
    form_class = ComplicationCreateForm
    success_url = reverse_lazy("tracker:complication-list")

    def get(self, request, *args, **kwargs):
        vaccination_id = self.kwargs.get('pk')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        vaccination = get_object_or_404(Vaccination, pk=self.kwargs['pk'])
        form.instance.vaccination = vaccination
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context


class ComplicationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Complication
    fields = ("description", )
    success_url = reverse_lazy("tracker:complication-list")


class ComplicationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Complication
    success_url = reverse_lazy("tracker:complication-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context





from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from tracker.forms import (
    VaccinationCreateForm,
    ComplicationCreateForm,
    ParentCreationForm,
)
from tracker.models import Child, Parent, Vaccine, Vaccination, Complication


def index(request):
    num_children = Child.objects.count()
    num_parents = Parent.objects.count()
    num_complications = Complication.objects.count()

    context = {
        "num_children": num_children,
        "num_parents": num_parents,
        "num_complications": num_complications,
    }

    return render(request, "tracker/index.html", context=context)


class VaccineListView(LoginRequiredMixin, generic.ListView):
    model = Vaccine
    queryset = Vaccine.objects.all()
    template_name = "tracker/vaccine_list.html"


class ChildListView(LoginRequiredMixin, generic.ListView):
    model = Child
    queryset = Child.objects.prefetch_related("vaccinations__vaccine")
    template_name = "tracker/child_list.html"


class ChildDetailView(generic.DetailView, LoginRequiredMixin):
    model = Child
    queryset = Child.objects.prefetch_related("vaccinations")
    template_name = "tracker/child_detail.html"


class ChildCreateView(generic.CreateView, LoginRequiredMixin):
    model = Child
    fields = ("first_name", "last_name", "gender", "birth_date")
    success_url = reverse_lazy("tracker:child-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context

    def form_valid(self, form):
        form.instance.parent = self.request.user
        return super().form_valid(form)


class ChildUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Child
    fields = ("first_name", "last_name", "gender", "birth_date")
    success_url = reverse_lazy("tracker:child-list")


class ChildDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Child
    success_url = reverse_lazy("tracker:child-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context


class VaccinationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Vaccination
    template_name = "tracker/vaccination_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")

        return context


class VaccinationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Vaccination
    form_class = VaccinationCreateForm

    def get(self, request, *args, **kwargs):
        kwargs["child_id"] = self.kwargs.get("pk")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        child = get_object_or_404(Child, pk=self.kwargs["pk"])
        form.instance.child = child
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context

    def get_success_url(self, **kwargs):
        return reverse(
            "tracker:child-detail", kwargs={"pk": self.kwargs["pk"]}
        )


class VaccinationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Vaccination
    fields = ("vaccine",)

    def get_success_url(self, **kwargs):
        return reverse(
            "tracker:vaccination-detail", kwargs={"pk": self.kwargs["pk"]}
        )


class VaccinationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Vaccination

    def get_success_url(self, **kwargs):
        return reverse(
            "tracker:child-detail", kwargs={"pk": self.kwargs["c_id"]}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context


class ComplicationListView(LoginRequiredMixin, generic.ListView):
    model = Complication
    template_name = "tracker/complication_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        print(context["previous_url"])
        if len(context["previous_url"].split("/")) >= 8:
            context["vaccine_id"] = context["previous_url"].split("/")[-4]
        elif len(context["previous_url"].split("/")) == 7:
            context["vaccine_id"] = context["previous_url"].split("/")[-3]
        else:
            context["vaccine_id"] = context["previous_url"].split("/")[-2]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        reference = self.request.META.get("HTTP_REFERER").split("/")
        if len(reference) == 8:
            some_value = reference[-4]
        elif len(reference) == 7:
            some_value = reference[-3]
        else:
            some_value = reference[-2]
        if some_value:
            queryset = queryset.filter(vaccination_id=some_value)
        return queryset


class ComplicationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Complication
    form_class = ComplicationCreateForm
    success_url = reverse_lazy("tracker:complication-list")

    def form_valid(self, form):
        vaccination = get_object_or_404(Vaccination, pk=self.kwargs["pk"])
        form.instance.vaccination = vaccination
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context


class ComplicationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Complication
    fields = ("description",)
    success_url = reverse_lazy("tracker:complication-list")


class ComplicationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Complication
    success_url = reverse_lazy("tracker:complication-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        return context


class ParentCreateView(generic.CreateView):
    model = Parent
    form_class = ParentCreationForm
    success_url = reverse_lazy("tracker:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        parent = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, parent)
        messages.success(
            self.request, "Thanks for registering. You are now logged in."
        )
        return response


class ParentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Parent
    template_name = "tracker/parent_detail.html"

    def get_success_url(self, **kwargs):
        return reverse(
            "tracker:parent-detail", kwargs={"pk": self.kwargs["pk"]}
        )

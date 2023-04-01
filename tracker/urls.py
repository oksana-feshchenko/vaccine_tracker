from django.urls import path

from tracker.views import (
    index,
    VaccineListView,
    ChildListView,
    ChildDetailView,
    VaccinationDetailView,
    ChildCreateView,
    ChildUpdateView,
    ChildDeleteView,
    ComplicationListView,
    VaccinationCreateView,
    VaccinationUpdateView,
    VaccinationDeleteView,
    ComplicationCreateView,
    ComplicationUpdateView,
    ComplicationDeleteView,
    ParentCreateView,
    ParentDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("schedule/", VaccineListView.as_view(), name="vaccine-list"),
    path("children/", ChildListView.as_view(), name="child-list"),
    path("children/<int:pk>/", ChildDetailView.as_view(), name="child-detail"),
    path("children/create/", ChildCreateView.as_view(), name="child-create"),
    path(
        "children/<int:pk>/update/",
        ChildUpdateView.as_view(),
        name="child-update",
    ),
    path(
        "children/<int:pk>/delete/",
        ChildDeleteView.as_view(),
        name="child-delete",
    ),
    path(
        "vaccination/<int:pk>/",
        VaccinationDetailView.as_view(),
        name="vaccination-detail",
    ),
    path(
        "children/<int:pk>/vaccination/create/",
        VaccinationCreateView.as_view(),
        name="vaccination-create",
    ),
    path(
        "vaccination/<int:pk>/update/",
        VaccinationUpdateView.as_view(),
        name="vaccination-update",
    ),
    path(
        "children/<int:c_id>/vaccination/<int:pk>/delete/",
        VaccinationDeleteView.as_view(),
        name="vaccination-delete",
    ),
    path(
        "complication/",
        ComplicationListView.as_view(),
        name="complication-list",
    ),
    path(
        "vaccination/<int:pk>/complication/create/",
        ComplicationCreateView.as_view(),
        name="complication-create",
    ),
    path(
        "complication/<int:pk>/update/",
        ComplicationUpdateView.as_view(),
        name="complication-update",
    ),
    path(
        "complication/<int:pk>/delete/",
        ComplicationDeleteView.as_view(),
        name="complication-delete",
    ),
    path("parent/create/", ParentCreateView.as_view(), name="parent-create"),
    path("parent/<int:pk>/", ParentDetailView.as_view(), name="parent-detail"),
]

app_name = "tracker"

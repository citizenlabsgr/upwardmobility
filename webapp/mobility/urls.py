from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("blog/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
    path("blog", views.PostListView.as_view(), name="post_list"),
    path('national-view', views.national_view, name="national_view"),
    path('county-details', views.county_details, name="county_details" ),
    path('county-rankings', views.county_finder, name="county_finder"),
    path('county-comparison', views.CountyComparison.as_view(), name="county_comparison"),
]
from django.urls import path
from .import views 

urlpatterns=[
    path("", views.HomePageView.as_view(), name="home"),
    path("about-us/", views.AboutPageView.as_view(), name="about-us"),
    path("blogs/", views.BlogsPageView.as_view(), name="blogs"),
    path("contact-us/", views.ContactPageView, name="contact-us"),
    path("subscribe/", views.Subscribe, name="subscribe"),
    path("membership/", views.membershipView, name="membership"),
    path("blog/<slug:slug>/", views.BlogDetailPageView.as_view(), name="blog-detail"),
]
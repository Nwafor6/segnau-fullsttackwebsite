from django.urls import path
from .import views 

urlpatterns=[
    path("", views.HomePageView.as_view(), name="home"),
    path("about-us/", views.AboutPageView.as_view(), name="about-us"),
    path("blogs/", views.BlogsPageView.as_view(), name="blogs"),
    path("contact-us/", views.ContactPageView, name="contact-us"),
    path("subscribe/", views.Subscribe, name="subscribe"),
    path("outreach/", views.OutreachPageView.as_view(), name="outreach"),
    path("seg-challenge-bowl/", views.ChallengebowlPageView.as_view(), name="challenge-bowl"),
    path("seg-conferences/", views.ComferencesPageView.as_view(), name="conferences"),
    path("fieldcamps/", views.FieldcampsPageView.as_view(), name="fieldcamps"),
    path("scholarships/", views.ScholarshipPageView.as_view(), name="scholarships"),
    path("leadership-symposium/", views.OutreachPageView.as_view(), name="symposium"),
    path("workshop&webniars/", views.workshopPageView.as_view(), name="workshop"),
    path("membership/", views.membershipView, name="membership"),
    path("blog/<slug:slug>/", views.BlogDetailPageView.as_view(), name="blog-detail"),
]
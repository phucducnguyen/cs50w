from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name = "index"),
    path("phuc",views.phuc, name = "phuc"),
    path("david",views.david, name = "david"),
    path("<str:name>",views.greet, name="greet"),
]
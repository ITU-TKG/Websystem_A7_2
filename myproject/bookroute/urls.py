from django.urls import path
from . import views

app_name="bookroute"
urlpatterns=[
    path("",views.index, name="index"),
    #bookrouteアプリのトップページ
    path("page/create/", views.page_create, name="page_create"),
    path("page/",views.page_list, name="page_list"),
    path("page/<uuid:id>/", views.page_detail, name="page_detail"),
    path("page/<uuid:id>/update/",views.page_update, name="page_update"),
    path('page/<uuid:pk>/delete/',views.PageDeleteView.as_view(), name="page_delete"),#追加1/20 変更点uuid:pk  !pk=primary key
]
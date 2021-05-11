from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    # Examples: /blog/
    path('', views.PostLV.as_view(), name='index'),

    # Examples: /blog/post/ (same as /blog/)
    path('post/', views.PostLV.as_view(), name='post_list'),

    # Examples: /blog/post/django_example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # Examples: /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # Examples: /blog/archive/2019/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # Examples: /blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # Examples: /blog/archive/2019/nov/10
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # Examples: /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    # Examples: /blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # Examples: /blog/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    # Examples: /blog/search/
    path('search/', views.SearchFormView.as_view(), name='search'),

    # Examples: /blog/add/
    path('add/', views.PostCreateView.as_view(), name='add',),

    # Examples: /blog/change/
    path('change/', views.PostCreateView.as_view(), name='add', ),
]
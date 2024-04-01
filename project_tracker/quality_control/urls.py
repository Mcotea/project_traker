from django.urls import path

from .views import *

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('bugs/', views.bug_list, name='bug_list'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),

    path('', IndexView.as_view(), name='index'),
    path('bugs/', bug_list, name='bug_list'),
    path('features/', feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', FeatureDetailView.as_view(), name='feature_detail'),
]

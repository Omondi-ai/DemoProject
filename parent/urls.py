from django.urls import path
from . import views

urlpatterns = [
    path('parent-dashboard', views.parent_dashboard, name="parent-dashboard"),
   
    path('browse-articles4', views.browse_articles, name="browse-articles4"),
   
    path('account-management4', views.account_management, name="account-management4"),

    path('delete-account4', views.delete_account, name='delete-account4'),
    # subscriptions



]
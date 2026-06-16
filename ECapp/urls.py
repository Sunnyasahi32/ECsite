from django.urls import path
from . import views

app_name = "ECapp" 

urlpatterns = [
    path("login/", views.login.as_view(), name = 'login'),
    path("registerUser/", views.register_user.as_view(), name = 'register_user'),
    path("registerUserConfirm/", views.register_user_confirm.as_view(), name = 'register_user_confirm'),
    path("registerUserCommit/", views.register_user_commit.as_view(), name = 'register_user_commit'),
    path("logout/", views.logout.as_view(), name = 'logout'),
    path("cart/", views.cart.as_view(), name = 'cart'),
    path("userInfo/", views.user_info.as_view(), name = 'user_info'),
    path("updateUser/", views.update_user.as_view(), name = 'update_user'),
    path("updateUserConfirm/", views.update_user_confirm.as_view(), name = 'update_user_confirm'),
    path("updateUserCmmit/", views.update_user_commit.as_view(), name = 'update_user_commit'),
    path("withDrawConfirm/", views.with_draw_confirm.as_view(), name = 'with_draw_confirm'),
    path("searchResult/", views.search_result.as_view(), name = 'search_result'),
    path("itemDetail/<int:item_id>/", views.item_detail.as_view(), name = 'item_detail'),

    
    path("", views.main.as_view(), name = 'main'),
]
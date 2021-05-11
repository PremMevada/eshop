from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "apps.seller_accounts"
urlpatterns = [
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('signout/',views.signout, name="signout"),
    path('profile/',views.profile, name="profile"),
    path('company_info/',views.companyinfo, name="companyinfo"),
    path('company_details/',views.company_details, name="company_details"),
    path('company_sales/',views.companysales, name="companysales"),
    path('company_products/',views.companyproducts, name="companyproducts"),
    path('add_new_product/',views.addnewproduct, name="add_new_product"),
    path('edit_product/<int:proid>/',views.editproduct, name="edit_product"),
    path('add_single_product',views.add_single_product,name="add_single_product"),
    path('add_multiple_product',views.add_multiple_products,name="add_multiple_products"),
    path('addressinfo/',views.address_info, name="address_info"),
    path('orders/',views.orders, name="sellerorders")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
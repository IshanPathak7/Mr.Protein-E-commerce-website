from app.forms import LoginForm, MyPasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('cart/', views.show_cart, name='showcart'),
    path('add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm), name='passwordchange'),
    path('product/<int:pk>', views.product, name='product'),
    path('tutorial/<int:pk>', views.show_tutorial, name='show_tutorial'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('accounts/', include('django.contrib.auth.urls'))

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

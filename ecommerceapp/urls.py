from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('loginn',views.loginn,name='loginn'),
    path('login1',views.login1,name='login1'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('userhome',views.userhome,name='userhome'),
    path('logoutt',views.logoutt,name='logoutt'),
    path('signup',views.signup,name='signup'),
    path('signupaction',views.signupaction,name='signupaction'),
    path('add_category',views.add_category,name='add_category'),
    path('addc',views.addc,name='addc'),
    path('add_product',views.add_product,name='add_product'),
    path('addp',views.addp,name='addp'),
    path('show_product',views.show_product,name='show_product'),
    path('show_user',views.show_user,name='show_user'),
    path('filtr/<int:pk>',views.filtr,name='filtr'),
    path('addtocart/<int:pk>',views.addtocart,name='addtocart'),
    path('cart',views.cart,name='cart'),
    path('remove1/<int:pk>',views.remove1,name='remove1'),
    path('deletep/<int:pk>',views.deletep,name='deletep'),
    path('deleteu/<int:pk>',views.deleteu,name='deleteu'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
"""lb_mngt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views
from django.conf.urls.static import  static
from django.conf import settings

from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
    path('register/',views.getloginpage),
    path('login/',views.getlogin),
    path('forgot/',views.forgot),
    path('search/',views.Book),
    path('all/',views.all,name="display_view"),
    path('details/',views.details),
    path('hello/',views.hello),
    # path('export/csv/', views.export_users_csv, name='export_users_csv'),
    # path('export/csv1/', views.csv1, name='csv1'),
    url(r'^bookedt/(?P<pk>\d+)/$',views.bookeditView.as_view()),
    url(r'^bookdelete/(?P<pk>\d+)/$',views.
    bookdlt.as_view()),
    url(r'^listview/$',views.listv.as_view()),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#url(r'search/', 'lb_mngt.views.search', name='search/')

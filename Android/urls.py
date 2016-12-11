"""Android URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from backstage import views as backstage_views
urlpatterns = [
    url(r'^login/$',backstage_views.login),
    url(r'^admin/', admin.site.urls),
    url(r'^first_category$', backstage_views.getFirstCategory),
    url(r'^second_category$', backstage_views.getSecondCategory),
    url(r'^product$', backstage_views.getProduct),
    url(r'^order$', backstage_views.getOrder),
    url(r'^productdetail',backstage_views.getProductDetail),
    url(r'^AddCart',backstage_views.AddCart),
    url(r'^QuerryCart',backstage_views.QuerryCart),
    url(r'^search$',backstage_views.search),
]

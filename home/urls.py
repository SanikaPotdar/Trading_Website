from django.urls import path
from home import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/', views.main, name='index'),
    path('charts/', views.charts, name='charts'),
    # path('', views.senti, name='senti'),
    path(r'investing_chart/', views.indian, name='in'),
    path('tables/', views.tables, name='tables'),
    path(r'login/', views.login1, name='login1'),
    path(r'grid/', views.crypto, name='crypto'),
    path(r'form-common/', views.form, name='form'),
    path(r'form-validation/', views.market, name='market'),
    path(r'news/', views.news, name='news'),
    # path(r'index/', views.back, name='back'),
]
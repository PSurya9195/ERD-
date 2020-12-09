from django.urls import path
from . import views

urlpatterns = [
  path('location/',views.get_location, name ='location'),
  path('r_list/<loc>',views.Restaurant_List, name='rlist'),
  path('res_food/<r_id>', views.Food_List, name ='flist'),
  path('registration/', views.register, name='register'),



  
  # path('api/', views.res_api),
  # path('food_api/', views.food_api),
]
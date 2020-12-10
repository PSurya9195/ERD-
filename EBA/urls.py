from django.urls import path
from . import views

# whenever a particular Url name got hit and it will search for linked view which has particular code and if there is link from view to template , those particular template also got executed

urlpatterns = [
  path('location/',views.get_location, name ='location'),
  path('r_list/<loc>',views.Restaurant_List, name='rlist'),
  path('res_food/<r_id>', views.Food_List, name ='flist'),
  path('registration/', views.register, name='register'),



  
  # path('api/', views.res_api),
  # path('food_api/', views.food_api),
]

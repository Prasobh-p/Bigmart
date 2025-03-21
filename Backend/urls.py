from django.urls import path
from Backend import views


urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('add_categ/',views.add_categ,name="add_categ"),
    path('save_categ/',views.save_categ,name="save_categ"),
    path('display_categ/',views.display_categ,name="display_categ"),
    path('edit_categ/<int:cid>/',views.edit_categ,name="edit_categ"),
    path('update_categ/<int:cid>/',views.update_categ,name="update_categ"),
    path('delete_categ/<int:cid>/',views.delete_categ,name="delete_categ"),
    path('admin/',views.admin,name="admin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('add_prod/',views.add_prod,name="add_prod"),
    path('save_prod/',views.save_prod,name="save_prod"),
    path('display_pro/',views.display_pro,name="display_pro"),
    path('edit_pro/<int:pid>/',views.edit_pro,name="edit_pro"),
    path('update_pro/<int:pid>/',views.update_pro,name="update_pro"),
    path('delete_pro/<int:pid>/',views.delete_pro,name="delete_pro"),
    path('contact_details',views.contact_details,name="contact_details")

]


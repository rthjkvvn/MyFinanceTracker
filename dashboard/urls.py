

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('users/', views.users, name='dashboard-users'),
    path('transaction/', views.transaction, name='dashboard-transaction'),
    path('category/', views.category, name='dashboard-category'),
    path('userreg/', views.userreg, name='userreg'),
    path('insertuser/', views.insertuser, name='insertuser'),
    path('userlist/', views.userlist, name='userlist'),
    path('deleteprofile/<int:id>', views.deleteprofile,name='deleteprofile'),
    path('useredit/<int:id>',views.useredit,name= 'useredit'),
    path('updateprofile/<int:id>', views.updateprofile, name='updateprofile'),
    path('viewtransaction/', views.viewtransaction, name='dashboard-transaction'),
<<<<<<< HEAD
    path('categoryreg/', views.categoryreg, name='categoryreg'),
    path('categorylist/', views.categorylist, name='categorylist'),
    path('insertcategory/', views.insertcategory, name='insertcategory'),
    path('categoryedit/<int:id>',views.categoryedit,name= 'categoryedit'),
    path('updatecategory/<int:id>', views.updatecategory, name='updatecategory')

=======
    path('categoryreg/', views.categoryreg, name='categoryreg')
>>>>>>> 6df282d63f60d85ee491f240f0d46cb6c7828add
]  


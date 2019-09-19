from main import views


app_name = 'main'

urlpatterns = [
    path('main/', views.WhatsappGroupsView.as_view(), name='main'),
]

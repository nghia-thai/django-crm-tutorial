from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from customer.views import CustomerCreate, CustomerDelete, CustomerDetail, CustomerUpdate, Customerlist


schema_view = get_schema_view(
    openapi.Info(
        title='CRM API',
        default_version='v1',
        description='Description',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', Customerlist.as_view()),
    path('create/', CustomerCreate.as_view(), name='create-customer'),
    path('<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'),
    path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]
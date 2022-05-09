from django.urls import path, include

urlpatterns = [
    path("agents/", include("agent.urls")),
    path("users/", include("administrator.urls")),
    path("clients/", include("client.urls")),
    path("products/", include("policies.urls")),
    path("account/", include("accounts.urls")),
    path("products/type/", include("lifeInsurance.urls")),
    path("products/type/", include("healthInsurance.urls")),
    path("products/type/", include("motoInsurance.urls")),
]
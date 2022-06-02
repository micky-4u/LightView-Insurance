from django.urls import path, include

urlpatterns = [
    path("agents/", include("agent.urls")),
    path("", include("administrator.urls")),
    path("clients/", include("client.urls")),
    path("/", include("policies.urls")),
    path("accounts/", include("accounts.urls")),
    path("products/type/life/", include("lifeInsurance.urls")),
    path("products/type/health/", include("healthInsurance.urls")),
    path("products/type/moto/", include("motoInsurance.urls")),
    path("products/type/home/", include("homeInsurance.urls")),
]
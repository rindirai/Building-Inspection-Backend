from django.urls import path
from . import views
from .views import get_all_client_profiles, get_all_client_profiles_simple, get_client_profile, client_profile_status_counts, client_profile_status_monthly_counts, top_rated_clients, client_profile_by_status

urlpatterns = [
    path('create-client', views.client_with_stages, name='create-client'),
    # Update Foundation Inspection
    path('update-foundation/', views.update_foundation_inspection,
         name='update-foundation'),

    # Update Framing Inspection
    path('update-framing/', views.update_framing_inspection, name='update-framing'),

    # Update Electrical Inspection
    path('update-electrical/', views.update_electrical_inspection,
         name='update-electrical'),

    # Update Plumbing Inspection
    path('update-plumbing/', views.update_plumbing_inspection,
         name='update-plumbing'),

    # Update HVAC Inspection
    path('update-hvac/', views.update_hvac_inspection, name='update-hvac'),

    # Update Insulation Inspection
    path('update-insulation/', views.update_insulation_inspection,
         name='update-insulation'),

    # Update Drywall Inspection
    path('update-drywall/', views.update_drywall_inspection, name='update-drywall'),

    # Update Final Inspection
    path('update-final/', views.update_final_inspection, name='update-final'),

    # Get all ClientProfiles
    path('client-profiles/', get_all_client_profiles.as_view(),
         name='get-all-client-profiles'),

    path('client-profiles-simple/', get_all_client_profiles_simple.as_view(),
         name='get-all-client-profiles-simple'),

    # Get a single ClientProfile by ID
    path('client-profiles/<int:pk>/',
         get_client_profile.as_view(), name='get-client-profile'),

    path('status-client-profiles/<str:status>/',
         client_profile_by_status.as_view(), name='get-client-profile-by-status'),

    path('count-profiles/', client_profile_status_counts.as_view(),
         name='count-profiles'),

    path('profiles-month/', client_profile_status_monthly_counts.as_view(),
         name='profiles_month'),
    path('top-rated/', top_rated_clients.as_view(),
         name='top-rated'),

    # Update Client Profile
    path('update-client-profile/',
         views.update_client_profile, name='update-drywall'),

]

from django.contrib import admin
from .models import ClientProfile, InspectionStage, FoundationInspection, FramingInspection, ElectricalInspection, PlumbingInspection, HVACInspection, InsulationInspection, DrywallInspection, FinalInspection

# Register your models here.


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address',
                    'location', 'inspection_status', 'inspection_level')
    search_fields = ('name', 'email')


@admin.register(InspectionStage)
class InspectionStageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(FoundationInspection)
class FoundationInspectionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'client_profile', 'correct_excavation_depth', 'proper_soil_compaction_and_leveling',
                    'accurate_rebar_and_anchor_bolts_placement', 'is_completed', 'status')
    search_fields = ('stage__name', 'notes')


@admin.register(FramingInspection)
class FramingInspectionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'client_profile', 'plumb_and_aligned_wall_framing', 'level_and_structurally_sound_floor_framing',
                    'correctly_pitched_and_supported_roof_framing', 'is_completed', 'status')
    search_fields = ('stage__name', 'notes')


@admin.register(ElectricalInspection)
class ElectricalInspectionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'client_profile', 'matching_wire_size_and_type_for_circuits', 'correct_electrical_panel_installation_and_labeling',
                    'installation_of_gfci_and_afci_protection_where_needed', 'is_completed', 'status')
    search_fields = ('stage__name', 'notes')


@admin.register(PlumbingInspection)
class PlumbingInspectionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'client_profile', 'leak_free_and_correctly_sized_water_supply_lines', 'proper_slope_and_venting_in_drainage_systems',
                    'accurate_installation_of_plumbing_fixtures', 'is_completed', 'status')
    search_fields = ('stage__name', 'notes')


@admin.register(HVACInspection)
class HVACInspectionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'client_profile', 'correct_installation_of_heating_and_cooling_equipment', 'appropriately_sized_and_insulated_ductwork',
                    'adequate_ventilation_for_proper_air_circulation', 'is_completed', 'status')
    search_fields = ('stage__name', 'notes')


@admin.register(InsulationInspection)
class InsulationInspectionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'client_profile', 'gap_free_and_non_compressed_insulation_installation',
                    'insulation_with_required_thermal_r_values', 'correct_installation_of_vapor_barriers', 'is_completed', 'status')
    search_fields = ('stage__name', 'notes')


@admin.register(DrywallInspection)
class DrywallInspectionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'client_profile', 'secure_attachment_and_proper_securing_of_drywall',
                    'use_of_fire_resistant_drywall_where_required', 'correct_taping_and_mudding_of_seams', 'is_completed', 'status')
    search_fields = ('stage__name', 'notes')


@admin.register(FinalInspection)
class FinalInspectionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'client_profile', 'overall_structural_integrity_meets_standards',
                    'presence_of_safety_features_like_handrails', 'meeting_accessibility_requirements', 'is_completed', 'status')
    search_fields = ('stage__name', 'notes')

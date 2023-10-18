from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return filename.format(filename=filename)


class ClientProfile(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    email = models.CharField(blank=True, null=True, max_length=255)
    phone_number = models.CharField(blank=True, null=True, max_length=255)
    address = models.CharField(blank=True, null=True, max_length=255)
    location = models.CharField(blank=True, null=True, max_length=255)
    inspection_status = models.CharField(
        blank=True, null=True, max_length=255, default='Pending')
    inspection_level = models.CharField(blank=True, null=True, max_length=255)
    building_type = models.CharField(blank=True, null=True, max_length=255)
    rating = models.FloatField(null=True, blank=True, default=0)
    inspector = models.ForeignKey(
        User, related_name='inspector', on_delete=models.CASCADE, blank=True, null=True)
    # This field will be automatically set to the current date and time when an object is created
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Define a base model for Inspection Stage


class InspectionStage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Define a model for each inspection stage with Boolean fields for tasks


class FoundationInspection(models.Model):
    stage = models.ForeignKey(InspectionStage, on_delete=models.CASCADE)
    client_profile = models.ForeignKey(
        ClientProfile, related_name='foundation_inspection', on_delete=models.CASCADE)
    correct_excavation_depth = models.BooleanField(default=False)
    proper_soil_compaction_and_leveling = models.BooleanField(default=False)
    accurate_rebar_and_anchor_bolts_placement = models.BooleanField(
        default=False)
    well_installed_formwork_and_bracing = models.BooleanField(default=False)
    adequate_curing_and_moisture_control = models.BooleanField(default=False)
    consistent_reinforcement_spacing = models.BooleanField(default=False)
    compliant_concrete_mix = models.BooleanField(default=False)
    matching_foundation_dimensions_with_plans = models.BooleanField(
        default=False)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.stage.name


class FramingInspection(models.Model):
    stage = models.ForeignKey(InspectionStage, on_delete=models.CASCADE)
    client_profile = models.ForeignKey(
        ClientProfile, related_name='framing_inspection', on_delete=models.CASCADE)
    plumb_and_aligned_wall_framing = models.BooleanField(default=False)
    level_and_structurally_sound_floor_framing = models.BooleanField(
        default=False)
    correctly_pitched_and_supported_roof_framing = models.BooleanField(
        default=False)
    proper_use_of_fasteners_and_connectors = models.BooleanField(default=False)
    meeting_load_bearing_requirements = models.BooleanField(default=False)
    adherence_to_framing_spacing_plans = models.BooleanField(default=False)
    adequately_sized_and_installed_header_beams = models.BooleanField(
        default=False)
    compliant_fire_blocking_installed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)


class ElectricalInspection(models.Model):
    stage = models.ForeignKey(InspectionStage, on_delete=models.CASCADE)
    client_profile = models.ForeignKey(
        ClientProfile, related_name='electrical_inspection', on_delete=models.CASCADE)
    matching_wire_size_and_type_for_circuits = models.BooleanField(
        default=False)
    correct_electrical_panel_installation_and_labeling = models.BooleanField(
        default=False)
    present_grounding_and_bonding_systems = models.BooleanField(default=False)
    installation_of_gfci_and_afci_protection_where_needed = models.BooleanField(
        default=False)
    compliance_with_local_electrical_codes = models.BooleanField(default=False)
    proper_outlet_spacing_as_per_regulations = models.BooleanField(
        default=False)
    correct_installation_of_conduit_and_junction_boxes = models.BooleanField(
        default=False)
    defect_free_wiring = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)


class PlumbingInspection(models.Model):
    stage = models.ForeignKey(InspectionStage, on_delete=models.CASCADE)
    client_profile = models.ForeignKey(
        ClientProfile, related_name='plumbing_inspection', on_delete=models.CASCADE)
    leak_free_and_correctly_sized_water_supply_lines = models.BooleanField(
        default=False)
    proper_slope_and_venting_in_drainage_systems = models.BooleanField(
        default=False)
    accurate_installation_of_plumbing_fixtures = models.BooleanField(
        default=False)
    use_of_code_compliant_pipe_materials = models.BooleanField(default=False)
    presence_of_required_p_traps_and_cleanouts = models.BooleanField(
        default=False)
    compliance_with_local_plumbing_codes = models.BooleanField(default=False)
    successful_pressure_testing = models.BooleanField(default=False)
    installation_of_backflow_prevention_devices_where_required = models.BooleanField(
        default=False)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)

# Define a model for HVAC Inspection


class HVACInspection(models.Model):
    stage = models.ForeignKey(InspectionStage, on_delete=models.CASCADE)
    client_profile = models.ForeignKey(
        ClientProfile, related_name='hvac_inspection', on_delete=models.CASCADE)
    correct_installation_of_heating_and_cooling_equipment = models.BooleanField(
        default=False)
    appropriately_sized_and_insulated_ductwork = models.BooleanField(
        default=False)
    adequate_ventilation_for_proper_air_circulation = models.BooleanField(
        default=False)
    meeting_energy_efficiency_standards = models.BooleanField(default=False)
    adherence_to_safety_regulations_for_combustion_appliances = models.BooleanField(
        default=False)
    performance_of_system_balancing = models.BooleanField(default=False)
    proper_installation_of_air_filters = models.BooleanField(default=False)
    functioning_thermostats_and_controls = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)

# Define a model for Insulation Inspection


class InsulationInspection(models.Model):
    stage = models.ForeignKey(InspectionStage, on_delete=models.CASCADE)
    client_profile = models.ForeignKey(
        ClientProfile, related_name='insulation_inspection', on_delete=models.CASCADE)
    gap_free_and_non_compressed_insulation_installation = models.BooleanField(
        default=False)
    insulation_with_required_thermal_r_values = models.BooleanField(
        default=False)
    use_of_fire_rated_insulation_where_needed = models.BooleanField(
        default=False)
    correct_installation_of_vapor_barriers = models.BooleanField(default=False)
    compliance_with_fire_safety_standards_for_insulation = models.BooleanField(
        default=False)
    insulation_thickness_matching_plans = models.BooleanField(default=False)
    presence_of_specified_soundproofing_insulation = models.BooleanField(
        default=False)
    insulation_material_matching_specifications = models.BooleanField(
        default=False)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)

# Define a model for Drywall Inspection


class DrywallInspection(models.Model):
    stage = models.ForeignKey(InspectionStage, on_delete=models.CASCADE)
    client_profile = models.ForeignKey(
        ClientProfile, related_name='drywall_inspection', on_delete=models.CASCADE)
    secure_attachment_and_proper_securing_of_drywall = models.BooleanField(
        default=False)
    use_of_fire_resistant_drywall_where_required = models.BooleanField(
        default=False)
    correct_taping_and_mudding_of_seams = models.BooleanField(default=False)
    proper_finishing_of_corners_and_joints = models.BooleanField(default=False)
    drywall_thickness_as_specified = models.BooleanField(default=False)
    adherence_to_screw_spacing_standards_for_drywall = models.BooleanField(
        default=False)
    installation_of_necessary_wall_bracing = models.BooleanField(default=False)
    smooth_and_defect_free_drywall_surface = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)

# Define a model for Final Inspection


class FinalInspection(models.Model):
    stage = models.ForeignKey(InspectionStage, on_delete=models.CASCADE)
    client_profile = models.ForeignKey(
        ClientProfile, related_name='final_inspection', on_delete=models.CASCADE)
    overall_structural_integrity_meets_standards = models.BooleanField(
        default=False)
    presence_of_safety_features_like_handrails = models.BooleanField(
        default=False)
    meeting_accessibility_requirements = models.BooleanField(default=False)
    adherence_to_building_codes_and_regulations = models.BooleanField(
        default=False)
    permits_and_documentation_in_order = models.BooleanField(default=False)
    correct_installation_of_fire_safety_measures = models.BooleanField(
        default=False)
    proper_functioning_of_plumbing_and_electrical_systems = models.BooleanField(
        default=False)
    energy_efficiency_of_insulation_and_HVAC_systems = models.BooleanField(
        default=False)
    is_completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)

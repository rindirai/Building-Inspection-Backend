from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, generics
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from django.db.models.functions import ExtractYear
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User


from .models import ClientProfile, InspectionStage, FoundationInspection, FinalInspection, FramingInspection, ElectricalInspection, PlumbingInspection, HVACInspection, InsulationInspection, DrywallInspection
from .serializers import ClientProfileSerializer, InspectionStageSerializer, FoundationInspectionSerializer, FinalInspectionSerializer, FramingInspectionSerializer, ElectricalInspectionSerializer, PlumbingInspectionSerializer, HVACInspectionSerializer, InsulationInspectionSerializer, DrywallInspectionSerializer, ClientProfile2Serializer


@api_view(['POST'])
def client_with_stages(request):
    serializer = ClientProfileSerializer(data=request.data)
    if serializer.is_valid():
        # Get the user with the least inspector count
        user_with_least_inspectors = User.objects.annotate(
            inspector_count=Count('inspector')).order_by('inspector_count').first()

        # Set the inspector field in the serializer data
        serializer.validated_data['inspector'] = user_with_least_inspectors

        # Save the client profile with the assigned inspector
        client_profile = serializer.save()

        # Create InspectionStages for the client_profile
        inspection_stages = InspectionStage.objects.all()

        for stage in inspection_stages:
            if stage.name == 'Foundation':
                FoundationInspection.objects.create(
                    stage=stage, is_completed=False, status=False, client_profile=client_profile)
            elif stage.name == 'Framing':
                FramingInspection.objects.create(
                    stage=stage, is_completed=False, status=False, client_profile=client_profile)
            elif stage.name == 'Electrical':
                ElectricalInspection.objects.create(
                    stage=stage, is_completed=False, status=False, client_profile=client_profile)
            elif stage.name == 'Plumbing':
                PlumbingInspection.objects.create(
                    stage=stage, is_completed=False, status=False, client_profile=client_profile)
            elif stage.name == 'HVAC':
                HVACInspection.objects.create(
                    stage=stage, is_completed=False, status=False, client_profile=client_profile)
            elif stage.name == 'Insulation':
                InsulationInspection.objects.create(
                    stage=stage, is_completed=False, status=False, client_profile=client_profile)
            elif stage.name == 'Drywall':
                DrywallInspection.objects.create(
                    stage=stage, is_completed=False, status=False, client_profile=client_profile)
            elif stage.name == 'Final':
                FinalInspection.objects.create(
                    stage=stage, is_completed=False, status=False, client_profile=client_profile)

        print('user email')
        print(user_with_least_inspectors.email)

        # Send email to the assigned user
        email_subject = 'You Have Been Assigned a New Client Project'
        email_body = f'Congratulations! You have been assigned a new client.\n\nClient Name: {client_profile.name}\nClient Phone: {client_profile.phone_number}\nBuilding Type: {client_profile.building_type}'
        send_mail(email_subject, email_body, 'benjaminnyakambangwe@gmail.com',
                  [user_with_least_inspectors.email], fail_silently=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_foundation_inspection(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
        foundation_inspection = FoundationInspection.objects.get(
            client_profile=client_profile)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)
    except FoundationInspection.DoesNotExist:
        return Response({'detail': 'FoundationInspection not found for this ClientProfile.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = FoundationInspectionSerializer(
        foundation_inspection, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        # Check if is_completed is True after saving
        if foundation_inspection.is_completed:
            # Check if all the specified fields are True
            if (
                foundation_inspection.correct_excavation_depth and
                foundation_inspection.proper_soil_compaction_and_leveling and
                foundation_inspection.accurate_rebar_and_anchor_bolts_placement and
                foundation_inspection.well_installed_formwork_and_bracing and
                foundation_inspection.adequate_curing_and_moisture_control and
                foundation_inspection.consistent_reinforcement_spacing and
                foundation_inspection.compliant_concrete_mix and
                foundation_inspection.matching_foundation_dimensions_with_plans
            ):
                foundation_inspection.status = True
            else:
                foundation_inspection.status = False

            foundation_inspection.save()

            if foundation_inspection.status:
                email_body = 'Congratulation your inspection project have passed the Foundation Stage: \n\n' + \
                    foundation_inspection.notes
                send_mail('Foundation Stage Passed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
            else:
                email_body = 'We are sorry to inform you that your inspection project have failed the Foundation Stage: \n Consult the notes below from the inspector and schedule another inspection \n\n' + foundation_inspection.notes
                send_mail('Foundation Stage Failed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)

        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update Framing Inspection
@api_view(['PATCH'])
def update_framing_inspection(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
        framing_inspection = FramingInspection.objects.get(
            client_profile=client_profile)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)
    except FramingInspection.DoesNotExist:
        return Response({'detail': 'FramingInspection not found for this ClientProfile.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = FramingInspectionSerializer(
        framing_inspection, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        # Check if is_completed is True after saving
        if framing_inspection.is_completed:
            # Check if all the specified fields are True
            if (
                framing_inspection.plumb_and_aligned_wall_framing and
                framing_inspection.level_and_structurally_sound_floor_framing and
                framing_inspection.correctly_pitched_and_supported_roof_framing and
                framing_inspection.proper_use_of_fasteners_and_connectors and
                framing_inspection.meeting_load_bearing_requirements and
                framing_inspection.adherence_to_framing_spacing_plans and
                framing_inspection.adequately_sized_and_installed_header_beams and
                framing_inspection.compliant_fire_blocking_installed
            ):
                framing_inspection.status = True
            else:
                framing_inspection.status = False

            framing_inspection.save()

            if framing_inspection.status:
                email_body = 'Congratulation your inspection project have passed the Framing Stage: \n\n' + \
                    framing_inspection.notes
                send_mail('Framing Stage Passed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
            else:
                email_body = 'We are sorry to inform you that your inspection project have failed the Framing Stage: \n Consult the notes below from the inspector and schedule another inspection \n\n' + framing_inspection.notes
                send_mail('Framing Stage Failed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Electrical Inspection


@api_view(['PATCH'])
def update_electrical_inspection(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
        electrical_inspection = ElectricalInspection.objects.get(
            client_profile=client_profile)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)
    except ElectricalInspection.DoesNotExist:
        return Response({'detail': 'ElectricalInspection not found for this ClientProfile.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ElectricalInspectionSerializer(
        electrical_inspection, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        # Check if is_completed is True after saving
        if electrical_inspection.is_completed:
            # Check if all the specified fields are True
            if (
                electrical_inspection.matching_wire_size_and_type_for_circuits and
                electrical_inspection.correct_electrical_panel_installation_and_labeling and
                electrical_inspection.present_grounding_and_bonding_systems and
                electrical_inspection.installation_of_gfci_and_afci_protection_where_needed and
                electrical_inspection.compliance_with_local_electrical_codes and
                electrical_inspection.proper_outlet_spacing_as_per_regulations and
                electrical_inspection.correct_installation_of_conduit_and_junction_boxes and
                electrical_inspection.defect_free_wiring
            ):
                electrical_inspection.status = True
            else:
                electrical_inspection.status = False

            electrical_inspection.save()

            if electrical_inspection.status:
                email_body = 'Congratulation your inspection project have passed the Electrical Stage: \n\n' + \
                    electrical_inspection.notes
                send_mail('Electrical Stage Passed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
            else:
                email_body = 'We are sorry to inform you that your inspection project have failed the Electrical Stage: \n Consult the notes below from the inspector and schedule another inspection \n\n' + electrical_inspection.notes
                send_mail('Electrical Stage Failed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Plumbing Inspection


@api_view(['PATCH'])
def update_plumbing_inspection(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
        plumbing_inspection = PlumbingInspection.objects.get(
            client_profile=client_profile)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)
    except PlumbingInspection.DoesNotExist:
        return Response({'detail': 'PlumbingInspection not found for this ClientProfile.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PlumbingInspectionSerializer(
        plumbing_inspection, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        # Check if is_completed is True after saving
        if plumbing_inspection.is_completed:
            # Check if all the specified fields are True
            if (
                plumbing_inspection.leak_free_and_correctly_sized_water_supply_lines and
                plumbing_inspection.proper_slope_and_venting_in_drainage_systems and
                plumbing_inspection.accurate_installation_of_plumbing_fixtures and
                plumbing_inspection.use_of_code_compliant_pipe_materials and
                plumbing_inspection.presence_of_required_p_traps_and_cleanouts and
                plumbing_inspection.compliance_with_local_plumbing_codes and
                plumbing_inspection.successful_pressure_testing and
                plumbing_inspection.installation_of_backflow_prevention_devices_where_required
            ):
                plumbing_inspection.status = True
            else:
                plumbing_inspection.status = False

            plumbing_inspection.save()

            if plumbing_inspection.status:
                email_body = 'Congratulation your inspection project have passed the Plumbing Stage: \n\n' + \
                    plumbing_inspection.notes
                send_mail('Plumbing Stage Passed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
            else:
                email_body = 'We are sorry to inform you that your inspection project have failed the Plumbing Stage: \n Consult the notes below from the inspector and schedule another inspection \n\n' + plumbing_inspection.notes
                send_mail('Plumbing Stage Failed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update HVAC Inspection


@api_view(['PATCH'])
def update_hvac_inspection(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
        hvac_inspection = HVACInspection.objects.get(
            client_profile=client_profile)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)
    except HVACInspection.DoesNotExist:
        return Response({'detail': 'HVACInspection not found for this ClientProfile.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = HVACInspectionSerializer(
        hvac_inspection, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        # Check if is_completed is True after saving
        if hvac_inspection.is_completed:
            # Check if all the specified fields are True
            if (
                hvac_inspection.correct_installation_of_heating_and_cooling_equipment and
                hvac_inspection.appropriately_sized_and_insulated_ductwork and
                hvac_inspection.adequate_ventilation_for_proper_air_circulation and
                hvac_inspection.meeting_energy_efficiency_standards and
                hvac_inspection.adherence_to_safety_regulations_for_combustion_appliances and
                hvac_inspection.performance_of_system_balancing and
                hvac_inspection.proper_installation_of_air_filters and
                hvac_inspection.functioning_thermostats_and_controls
            ):
                hvac_inspection.status = True
            else:
                hvac_inspection.status = False

            hvac_inspection.save()

            if hvac_inspection.status:
                email_body = 'Congratulation your inspection project have passed the HVAC Stage: \n\n' + \
                    hvac_inspection.notes
                send_mail('HVAC Stage Passed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
            else:
                email_body = 'We are sorry to inform you that your inspection project have failed the HVAC Stage: \n Consult the notes below from the inspector and schedule another inspection \n\n' + hvac_inspection.notes
                send_mail('HVAC Stage Failed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Insulation Inspection


@api_view(['PATCH'])
def update_insulation_inspection(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
        insulation_inspection = InsulationInspection.objects.get(
            client_profile=client_profile)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)
    except InsulationInspection.DoesNotExist:
        return Response({'detail': 'InsulationInspection not found for this ClientProfile.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = InsulationInspectionSerializer(
        insulation_inspection, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        # Check if is_completed is True after saving
        if insulation_inspection.is_completed:
            # Check if all the specified fields are True
            if (
                insulation_inspection.gap_free_and_non_compressed_insulation_installation and
                insulation_inspection.insulation_with_required_thermal_r_values and
                insulation_inspection.use_of_fire_rated_insulation_where_needed and
                insulation_inspection.correct_installation_of_vapor_barriers and
                insulation_inspection.compliance_with_fire_safety_standards_for_insulation and
                insulation_inspection.insulation_thickness_matching_plans and
                insulation_inspection.presence_of_specified_soundproofing_insulation and
                insulation_inspection.insulation_material_matching_specifications
            ):
                insulation_inspection.status = True
            else:
                insulation_inspection.status = False

            insulation_inspection.save()

            if insulation_inspection.status:
                email_body = 'Congratulation your inspection project have passed the Insulation Stage: \n\n' + \
                    insulation_inspection.notes
                send_mail('Insulation Stage Passed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
            else:
                email_body = 'We are sorry to inform you that your inspection project have failed the Insulation Stage: \n Consult the notes below from the inspector and schedule another inspection \n\n' + insulation_inspection.notes
                send_mail('Insulation Stage Failed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Drywall Inspection


@api_view(['PATCH'])
def update_drywall_inspection(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
        drywall_inspection = DrywallInspection.objects.get(
            client_profile=client_profile)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)
    except DrywallInspection.DoesNotExist:
        return Response({'detail': 'DrywallInspection not found for this ClientProfile.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = DrywallInspectionSerializer(
        drywall_inspection, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        # Check if is_completed is True after saving
        if drywall_inspection.is_completed:
            # Check if all the specified fields are True
            if (
                drywall_inspection.secure_attachment_and_proper_securing_of_drywall and
                drywall_inspection.use_of_fire_resistant_drywall_where_required and
                drywall_inspection.correct_taping_and_mudding_of_seams and
                drywall_inspection.proper_finishing_of_corners_and_joints and
                drywall_inspection.drywall_thickness_as_specified and
                drywall_inspection.adherence_to_screw_spacing_standards_for_drywall and
                drywall_inspection.installation_of_necessary_wall_bracing and
                drywall_inspection.smooth_and_defect_free_drywall_surface
            ):
                drywall_inspection.status = True
            else:
                drywall_inspection.status = False

            drywall_inspection.save()

            if drywall_inspection.status:
                email_body = 'Congratulation your inspection project have passed the Drywall Stage: \n\n' + \
                    drywall_inspection.notes
                send_mail('Drywall Stage Passed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
            else:
                email_body = 'We are sorry to inform you that your inspection project have failed the Drywall Stage: \n Consult the notes below from the inspector and schedule another inspection \n\n' + drywall_inspection.notes
                send_mail('Drywall Stage Failed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Final Inspection


@api_view(['PATCH'])
def update_final_inspection(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
        final_inspection = FinalInspection.objects.get(
            client_profile=client_profile)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)
    except FinalInspection.DoesNotExist:
        return Response({'detail': 'FinalInspection not found for this ClientProfile.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = FinalInspectionSerializer(
        final_inspection, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        # Check if is_completed is True after saving
        if final_inspection.is_completed:
            # Check if all the specified fields are True
            if (
                final_inspection.overall_structural_integrity_meets_standards and
                final_inspection.presence_of_safety_features_like_handrails and
                final_inspection.meeting_accessibility_requirements and
                final_inspection.adherence_to_building_codes_and_regulations and
                final_inspection.permits_and_documentation_in_order and
                final_inspection.correct_installation_of_fire_safety_measures and
                final_inspection.proper_functioning_of_plumbing_and_electrical_systems and
                final_inspection.energy_efficiency_of_insulation_and_HVAC_systems
            ):
                final_inspection.status = True
            else:
                final_inspection.status = False

            final_inspection.save()

            if final_inspection.status:
                email_body = 'Congratulation your inspection project have passed the Final Stage: \n\n' + \
                    final_inspection.notes
                send_mail('Final Stage Passed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
            else:
                email_body = 'We are sorry to inform you that your inspection project have failed the Final Stage: \n Consult the notes below from the inspector and schedule another inspection \n\n' + final_inspection.notes
                send_mail('Final Stage Failed', email_body, 'benjaminnyakambangwe@gmail.com',
                          [client_profile.email], fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get all ClientProfiles
class get_all_client_profiles(generics.ListAPIView):
    queryset = ClientProfile.objects.all().prefetch_related(
        'foundation_inspection', 'framing_inspection')
    serializer_class = ClientProfile2Serializer


class get_all_client_profiles_simple(generics.ListAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

# Get a single ClientProfile by ID


class get_client_profile(generics.RetrieveAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfile2Serializer


class client_profile_status_counts(generics.ListAPIView):
    serializer_class = ClientProfileSerializer

    def get_queryset(self):
        # Define a list of all possible inspection_status values
        status_values = ['null', 'active', 'passed', 'failed', 'pending']

        # Query the database to count ClientProfiles with each status
        queryset = ClientProfile.objects.values('inspection_status') \
            .annotate(count=Count('id'))

        # Create a list to store the counts
        status_counts = [{'inspection_status': status, 'count': 0}
                         for status in status_values]

        # Update the status_counts list with counts from the queryset
        for item in queryset:
            inspection_status = item['inspection_status']
            if inspection_status is None:
                # Handle None values
                for status_count in status_counts:
                    if status_count['inspection_status'] == 'null':
                        status_count['count'] = item['count']
            else:
                # Handle other status values
                for status_count in status_counts:
                    if status_count['inspection_status'] == inspection_status:
                        status_count['count'] = item['count']

        return status_counts

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        response_data = {item['inspection_status']: item['count'] for item in queryset}

        return Response(response_data)


class client_profile_status_monthly_counts(generics.ListAPIView):
    serializer_class = ClientProfileSerializer

    def get_queryset(self):
        # Filter profiles with "failed" and "passed" status
        queryset = ClientProfile.objects.filter(
            inspection_status__in=["failed", "passed"]
        )

        # Annotate the queryset to count profiles for each month
        queryset = queryset.annotate(
            month=ExtractMonth("date_added"),
        ).values("month", "inspection_status").annotate(
            count=Count("id")
        )

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        response_data = {
            "failed": [0] * 12,  # Initialize with 12 zeros
            "passed": [0] * 12,  # Initialize with 12 zeros
        }

        for item in queryset:
            status = item["inspection_status"]
            month = item["month"] - 1  # Adjust month to be 0-based index
            count = item["count"]

            response_data[status][month] = count

        return Response(response_data)


class top_rated_clients(generics.ListAPIView):
    serializer_class = ClientProfileSerializer

    def get_queryset(self):
        # Retrieve the top 6 rated clients based on the rating field
        queryset = ClientProfile.objects.exclude(
            rating=None).order_by('-rating')[:6]
        return queryset


class client_profile_by_status(generics.ListAPIView):
    serializer_class = ClientProfileSerializer

    def get_queryset(self):
        # Get the status from URL parameter
        status = self.kwargs.get('status', None)
        # Filter client profiles based on the inspection status
        queryset = ClientProfile.objects.filter(
            Q(inspection_status=status)
        )

        return queryset


# Update aclient Profile
@api_view(['PATCH'])
def update_client_profile(request):
    id = request.data['id']
    try:
        client_profile = ClientProfile.objects.get(id=id)
    except ClientProfile.DoesNotExist:
        return Response({'detail': 'ClientProfile not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClientProfileSerializer(
        client_profile, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

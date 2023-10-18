from rest_framework import serializers
from .models import ClientProfile, InspectionStage, FinalInspection, FoundationInspection, FramingInspection, InsulationInspection, DrywallInspection, ElectricalInspection, PlumbingInspection, HVACInspection


class InspectionStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionStage
        fields = '__all__'


class ClientProfileSerializer(serializers.ModelSerializer):
    inspection_stages = InspectionStageSerializer(many=True, read_only=True)

    class Meta:
        model = ClientProfile
        fields = '__all__'


class FoundationInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundationInspection
        fields = '__all__'


class FramingInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FramingInspection
        fields = '__all__'


class ElectricalInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricalInspection
        fields = '__all__'


class PlumbingInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlumbingInspection
        fields = '__all__'


class HVACInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HVACInspection
        fields = '__all__'


class InsulationInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsulationInspection
        fields = '__all__'


class DrywallInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrywallInspection
        fields = '__all__'


class FinalInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalInspection
        fields = '__all__'


# class ClientProfile2Serializer(serializers.ModelSerializer):
class ClientProfile2Serializer(serializers.ModelSerializer):
    foundation_inspection = FoundationInspectionSerializer(
        many=True, read_only=True)
    framing_inspection = FramingInspectionSerializer(many=True, read_only=True)
    electrical_inspection = ElectricalInspectionSerializer(
        many=True, read_only=True)
    plumbing_inspection = PlumbingInspectionSerializer(
        many=True, read_only=True)
    hvac_inspection = HVACInspectionSerializer(many=True, read_only=True)
    insulation_inspection = InsulationInspectionSerializer(
        many=True, read_only=True)
    drywall_inspection = DrywallInspectionSerializer(many=True, read_only=True)
    final_inspection = FinalInspectionSerializer(many=True, read_only=True)

    class Meta:
        model = ClientProfile
        fields = '__all__'

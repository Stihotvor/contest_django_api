from rest_framework import serializers

from netcovapp.models import Coverage


class CoverageSerializer(serializers.ModelSerializer):
    operator_name = serializers.CharField(source='operator.name', read_only=True)

    class Meta:
        model = Coverage
        fields = ['operator_name', 'net_2g', 'net_3g', 'net_4g']

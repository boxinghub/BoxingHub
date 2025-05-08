from rest_framework import serializers
from .models import Boxer, FightRecord, BoxerStats

class FightRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FightRecord
        fields = ['wins', 'losses', 'draws', 'wins_by_knockout', 'losses_by_knockout']

class BoxerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxerStats
        fields = ['strength', 'endurance', 'speed', 'reflex', 'boxing_iq', 'heart']

class BoxerSerializer(serializers.ModelSerializer):
    # NEST the related fields here
    fight_record = FightRecordSerializer(read_only=True)
    stats = BoxerStatsSerializer(read_only=True)

    class Meta:
        model = Boxer
        fields = [
            'id',
            'first_name',
            'last_name',
            'sex',
            'alias',
            'age',
            'nationality',
            'stance',
            'height_metric',
            'reach_metric',
            'height_imperial',
            'reach_imperial',
            'division',
            'fight_record',
            'stats'
        ]

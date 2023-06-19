from rest_framework import serializers

from .models import Employe, Pulpit


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ('name', 'last_name', 'otch', 'description',
                'email', 'puplit', 'post')
    

class PulpitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pulpit
        fields = ('slug', 'puplit')
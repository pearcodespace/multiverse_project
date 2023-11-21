from rest_framework import serializers
from .models import Text, CSVFile

class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFile
        fields = '__all__'

class TextSerializer(serializers.ModelSerializer):
    csv_file = CSVFileSerializer()

    class Meta:
        model = Text
        fields = '__all__'

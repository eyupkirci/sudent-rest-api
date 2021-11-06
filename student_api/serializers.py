# class StudentSerializerWithSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)

from rest_framework import serializers
from .models import Student, Path

class PathSerializer(serializers.ModelSerializer):
    # students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # students = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     many=True,
    #     view_name='detail'
    #     )
    
    class Meta:
        model = Path
        fields ='__all__'



class StudentSerializer(serializers.ModelSerializer):
    path=serializers.StringRelatedField()
    path_id=serializers.IntegerField()
    paths=serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "number", "path", "path_id", "paths"]
        # fields = '__all__'
        # exclude = ['number']
    def get_paths(self,obj):
        paths_data=Path.objects.all()
        serializer = PathSerializer(paths_data, many=True)
        
        return serializer.data
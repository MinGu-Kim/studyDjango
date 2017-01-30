from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# ★웹 API를 만들려면 우선 Snippet 클래스의 인스턴스를 json 같은 형태로 직렬화(serializing)하거나 반직렬화(deserializing)할 수 있어야 합니다.
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    # pk = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    #
    # def create(self, validated_data):
    #     """
    #     검증한 데이터로 새 `Snippet` 인스턴스를 생성하여 리턴합니다.
    #     """
    #     return Snippet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     검증한 데이터로 기존 `Snippet` 인스턴스를 업데이트한 후 리턴합니다.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance
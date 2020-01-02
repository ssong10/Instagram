from rest_framework import serializers
from .models import Hashtag, Article, Comment

class HashtagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['content',]

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'image', 'content', 'created_at', 'like_user', 'user', 'hashtag']

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'created_at']

class ArticleDeailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializers(many=True)
    class Meta(ArticleSerializers.Meta):
        fields = ArticleSerializers.Meta.fields + ['comment_set']

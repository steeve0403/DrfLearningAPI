from rest_framework import serializers

from shop.models import Category, Product, Article




class ProductSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']


class CategorySerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductSerialiser(queryset, many=True)
        return serializer.data
from rest_framework import serializers

from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "categories",
            "categories_id",
        ]

from rest_framework import serializers
from sea_distributor.models import Distributor
from sea_supplier.models import Supplier
from user_profile.models import User

from hashid_field.rest import HashidSerializerCharField


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'company_name', 'phone', 'address', 'role']

class SupplierSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field='sea_supplier.Supplier.id', read_only=True)
    class Meta:
        model = Supplier
        fields = ['id']


class ItemListSerializer(serializers.ModelSerializer):
    item_id = SupplierSerializer(read_only=True)

    class Meta:
        model = Distributor
        fields = ['item_id', 'created']


class ItemDetailsSericalizer(serializers.ModelSerializer):
    item_id = SupplierSerializer(read_only=True)
    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Distributor
        exclude = ['id']

class ItemRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        exclude = ['id', 'created', 'item_id', 'user']


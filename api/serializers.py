from rest_framework import serializers
from books.models import Book

# class SenzSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Senz
#         fields = ['device_uuid', 'port_id', 'utc_timestamp', 'sensor_id', 'sensor_settings', 'firmware_id',
#                   'product_id', 'target_id', 'protocol_version', 'firmware_crc', 'dest_uuid', 'dest_port_id',
#                   'uptime', 'status', 'online_time']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')

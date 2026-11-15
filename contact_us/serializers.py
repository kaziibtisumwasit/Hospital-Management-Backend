from rest_framework import serializers
from .models import ContactUs

## models.py er model er data ghula Serializer er moddhome JS er object Notation ba JSON e convert hoye jabe
## ei json ta ei front er shate backend er communication mediam
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta: ## class Meta is use to add characteristics to the serializer class. It allows you to specify options such as the model to be serialized, the fields to include or exclude, and other settings related to serialization.
        model = ContactUs ## model er name ta string hisabe deya hoyeche
        fields = "__all__" ## ei serializer er moddhome model er sob field gula ke serialize kora hobe


## Model Object -->> JSON Object -->> JSON Data -->> JSON String -->> Frontend
from django.db import migrations


def add_sample_pets(apps, schema_editor):
    Pet = apps.get_model('pets', 'Pet')
    sample_pets = [
        {
            'name': 'Coco',
            'animal_type': 'Dog',
            'age': 2,
            'description': 'Friendly, playful and fond of walks.',
        },
        {
            'name': 'Milo',
            'animal_type': 'Cat',
            'age': 1,
            'description': 'Curious, gentle and happiest near a sunny window.',
        },
        {
            'name': 'Pepper',
            'animal_type': 'Rabbit',
            'age': 3,
            'description': 'Calm little explorer who loves leafy greens.',
        },
    ]
    for pet in sample_pets:
        Pet.objects.get_or_create(name=pet['name'], defaults=pet)


def remove_sample_pets(apps, schema_editor):
    Pet = apps.get_model('pets', 'Pet')
    Pet.objects.filter(name__in=['Coco', 'Milo', 'Pepper']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('pets', '0002_adoptionrequest'),
    ]

    operations = [
        migrations.RunPython(add_sample_pets, remove_sample_pets),
    ]

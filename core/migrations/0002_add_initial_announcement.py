from django.db import migrations


def create_initial_announcement(apps, schema_editor):
    Announcement = apps.get_model('core', 'Announcement')
    # Only create if none exist to avoid duplicates on re-run
    if not Announcement.objects.exists():
        Announcement.objects.create(
            title='Simple Announcement',
            short_content='This is a short announcement. Click Read more.',
            content=(
                'HELLOOOOOOOOODSAKLD '
                'Read more. You can toggle to show less as well.'
            ),
            is_published=True,
        )


def noop(apps, schema_editor):
    # No-op reverse migration
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_announcement, noop),
    ]



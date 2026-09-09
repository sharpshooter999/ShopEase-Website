from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keyur', '0003_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
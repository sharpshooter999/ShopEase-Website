from django.db import migrations


def seed_stock(apps, schema_editor):
    Product = apps.get_model('keyur', 'Product')
    for product in Product.objects.order_by('id'):
        if product.id % 5 == 0:
            product.stock = 1
        elif product.id % 3 == 0:
            product.stock = 2
        else:
            product.stock = 8
        product.save(update_fields=['stock'])


class Migration(migrations.Migration):

    dependencies = [
        ('keyur', '0004_product_stock'),
    ]

    operations = [
        migrations.RunPython(seed_stock, migrations.RunPython.noop),
    ]
# Generated by Django 3.2.25 on 2025-05-23 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_review', models.TextField(max_length=400)),
                ('experience_review', models.TextField(max_length=400)),
                ('rating', models.IntegerField(choices=[(5, '5 *'), (4, '4 *'), (3, '3 *'), (2, '2 *'), (1, '1 *'), (0, '0 *')], default=5)),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]

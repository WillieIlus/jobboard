# Generated by Django 4.2.3 on 2023-07-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('price_per_day', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='price per day')),
                ('trial_period', models.IntegerField(blank=True, null=True, verbose_name='trial period')),
                ('is_default', models.BooleanField(default=False, verbose_name='is default')),
                ('is_fallback', models.BooleanField(default=False, verbose_name='is fallback')),
                ('is_available', models.BooleanField(default=True, verbose_name='is available')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_featured', models.BooleanField(default=False, verbose_name='is featured')),
                ('weight', models.IntegerField(default=0, verbose_name='weight')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
            options={
                'verbose_name_plural': 'Plans',
                'ordering': ['weight'],
            },
        ),
    ]

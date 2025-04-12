# Generated by Django 5.1.7 on 2025-04-11 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Abonnement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etrangere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
                ('genre', models.CharField(choices=[('A', 'Autres'), ('F', 'Feminin'), ('M', 'Masculin')], max_length=1)),
                ('CNI', models.CharField(max_length=20)),
                ('abonnement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Abonnement.abonnement')),
            ],
        ),
    ]

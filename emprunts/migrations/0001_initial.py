# Generated by Django 5.1.7 on 2025-04-14 09:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Etrangeres', '0001_initial'),
        ('livre', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(default=datetime.date.today)),
                ('date_fin_emprunt', models.DateField(null=True)),
                ('rendu', models.BooleanField(default=False)),
                ('etrangere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Etrangeres.etrangere')),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livre.livre')),
            ],
        ),
    ]

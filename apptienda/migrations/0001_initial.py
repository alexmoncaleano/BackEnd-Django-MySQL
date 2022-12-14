# Generated by Django 4.1.2 on 2022-10-11 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('añoedicion', models.CharField(max_length=20)),
                ('preciocompra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precioalquiler', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponible', models.BooleanField()),
                ('portada', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=25, verbose_name='apellido')),
                ('cedula', models.CharField(max_length=20, verbose_name='cedula')),
                ('direcion', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contraseña', models.CharField(max_length=12)),
                ('usuario', models.CharField(max_length=40)),
                ('persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apptienda.persona')),
            ],
        ),
        migrations.CreateModel(
            name='facturacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('valor', models.FloatField()),
                ('libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apptienda.libro')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apptienda.usuario')),
            ],
        ),
    ]

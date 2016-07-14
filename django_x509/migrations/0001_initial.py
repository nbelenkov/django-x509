# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-14 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_x509.models.base
import django_x509.models.ca
import jsonfield.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('notes', models.TextField(blank=True)),
                ('key_length', models.CharField(blank=True, choices=[('', ''), ('512', '512'), ('1024', '1024'), ('2048', '2048'), ('4096', '4096')], help_text='bits', max_length=6, verbose_name='key length')),
                ('digest', models.CharField(blank=True, choices=[('', ''), ('sha1', 'SHA1'), ('sha224', 'SHA224'), ('sha256', 'SHA256'), ('sha384', 'SHA384'), ('sha512', 'SHA512')], help_text='bits', max_length=8, verbose_name='digest algorithm')),
                ('validity_start', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('validity_end', models.DateTimeField(blank=True, default=django_x509.models.ca.default_ca_validity_end, null=True)),
                ('country_code', models.CharField(blank=True, max_length=2)),
                ('state', models.CharField(blank=True, max_length=64, verbose_name='state or province')),
                ('city', models.CharField(blank=True, max_length=64, verbose_name='city')),
                ('organization', models.CharField(blank=True, max_length=64, verbose_name='organization')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('common_name', models.CharField(blank=True, max_length=63, verbose_name='common name')),
                ('extensions', jsonfield.fields.JSONField(blank=True, default=list, help_text='additional x509 certificate extensions', verbose_name='extensions')),
                ('serial_number', models.PositiveIntegerField(blank=True, help_text='leave blank to determine automatically', null=True, verbose_name='serial number')),
                ('public_key', models.TextField(blank=True, help_text='certificate in X.509 PEM format')),
                ('private_key', models.TextField(blank=True, help_text='private key in X.509 PEM format')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'CA',
                'verbose_name_plural': 'CAs',
            },
        ),
        migrations.CreateModel(
            name='Cert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('notes', models.TextField(blank=True)),
                ('key_length', models.CharField(blank=True, choices=[('', ''), ('512', '512'), ('1024', '1024'), ('2048', '2048'), ('4096', '4096')], help_text='bits', max_length=6, verbose_name='key length')),
                ('digest', models.CharField(blank=True, choices=[('', ''), ('sha1', 'SHA1'), ('sha224', 'SHA224'), ('sha256', 'SHA256'), ('sha384', 'SHA384'), ('sha512', 'SHA512')], help_text='bits', max_length=8, verbose_name='digest algorithm')),
                ('validity_start', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('validity_end', models.DateTimeField(blank=True, default=django_x509.models.base.default_cert_validity_end, null=True)),
                ('country_code', models.CharField(blank=True, max_length=2)),
                ('state', models.CharField(blank=True, max_length=64, verbose_name='state or province')),
                ('city', models.CharField(blank=True, max_length=64, verbose_name='city')),
                ('organization', models.CharField(blank=True, max_length=64, verbose_name='organization')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('common_name', models.CharField(blank=True, max_length=63, verbose_name='common name')),
                ('extensions', jsonfield.fields.JSONField(blank=True, default=list, help_text='additional x509 certificate extensions', verbose_name='extensions')),
                ('serial_number', models.PositiveIntegerField(blank=True, help_text='leave blank to determine automatically', null=True, verbose_name='serial number')),
                ('public_key', models.TextField(blank=True, help_text='certificate in X.509 PEM format')),
                ('private_key', models.TextField(blank=True, help_text='private key in X.509 PEM format')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_x509.Ca', verbose_name='CA')),
            ],
            options={
                'verbose_name': 'certificate',
                'verbose_name_plural': 'certificates',
            },
        ),
        migrations.AlterUniqueTogether(
            name='cert',
            unique_together=set([('ca', 'serial_number')]),
        ),
    ]

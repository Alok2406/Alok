# Generated by Django 4.0.4 on 2022-07-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('head1', models.CharField(default='', max_length=50)),
                ('head1_cont', models.CharField(default='', max_length=3000)),
                ('sub_head2', models.CharField(default='', max_length=300)),
                ('shead2_cont', models.CharField(default='', max_length=3000)),
                ('sub_head3', models.CharField(default='', max_length=300)),
                ('shead3_cont', models.CharField(default='', max_length=3000)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
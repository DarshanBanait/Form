# Generated by Django 5.0.7 on 2024-09-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PHQGADResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('devices_used', models.CharField(max_length=255)),
                ('app_types', models.CharField(max_length=255)),
                ('main_screen_time_contributor', models.CharField(max_length=255)),
                ('screen_time_screenshot', models.ImageField(upload_to='screenshots/')),
                ('phq_question_1', models.IntegerField()),
                ('phq_question_2', models.IntegerField()),
                ('phq_question_3', models.IntegerField()),
                ('phq_question_4', models.IntegerField()),
                ('phq_question_5', models.IntegerField()),
                ('phq_question_6', models.IntegerField()),
                ('phq_question_7', models.IntegerField()),
                ('phq_question_8', models.IntegerField()),
                ('phq_question_9', models.IntegerField()),
                ('phq_total_score', models.IntegerField()),
                ('gad_question_1', models.IntegerField()),
                ('gad_question_2', models.IntegerField()),
                ('gad_question_3', models.IntegerField()),
                ('gad_question_4', models.IntegerField()),
                ('gad_question_5', models.IntegerField()),
                ('gad_question_6', models.IntegerField()),
                ('gad_question_7', models.IntegerField()),
                ('gad_total_score', models.IntegerField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

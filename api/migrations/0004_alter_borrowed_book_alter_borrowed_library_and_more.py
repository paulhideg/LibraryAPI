# Generated by Django 4.1.7 on 2023-03-26 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_borrowed_reader"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowed",
            name="book",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, to="api.book"
            ),
        ),
        migrations.AlterField(
            model_name="borrowed",
            name="library",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, to="api.library"
            ),
        ),
        migrations.AlterField(
            model_name="borrowed",
            name="reader",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, to="api.reader"
            ),
        ),
    ]

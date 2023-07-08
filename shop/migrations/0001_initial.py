# Generated by Django 4.2.2 on 2023-07-08 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('name', models.CharField(max_length=116)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinkType', models.CharField(choices=[('0', 'lạnh'), ('1', 'nóng')], default=0)),
                ('sizeType', models.CharField(choices=[('0', 'M'), ('1', 'L')], default=0)),
                ('sugarType', models.CharField(choices=[('0', '70%'), ('1', '30%'), ('2', '100%'), ('3', '50%'), ('4', 'Không đường')], default=0)),
                ('toppingType', models.CharField(choices=[('0', 'Trân trâu sương mai'), ('1', 'Trân châu hoàng kim'), ('2', 'Thạch Konjac'), ('3', 'Thạch cafe'), ('4', 'Thạch Machiato')], default=0)),
                ('price', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartItem', models.ManyToManyField(to='shop.cartitem')),
            ],
        ),
    ]

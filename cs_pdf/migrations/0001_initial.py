# Generated by Django 3.1.1 on 2020-09-25 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='书籍名称')),
                ('book_auth', models.CharField(max_length=100, verbose_name='作者')),
                ('book_publish_date', models.DateTimeField(verbose_name='发行日期')),
                ('book_brief', models.CharField(blank=True, max_length=100, null=True, verbose_name='一句话简概')),
                ('book_download', models.FileField(upload_to='pdf/', verbose_name='下载链接')),
                ('book_cover_img', models.ImageField(blank=True, null=True, upload_to='cover_img/', verbose_name='封面图片')),
                ('book_download_times', models.IntegerField(verbose_name='下载次数')),
                ('book_thumb_up', models.IntegerField(verbose_name='点赞次数')),
                ('book_detail', models.TextField(verbose_name='书籍介绍')),
                ('book_size', models.IntegerField(verbose_name='书籍大小')),
            ],
            options={
                'verbose_name': '书籍',
                'verbose_name_plural': '书籍',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='书籍分类')),
                ('index', models.IntegerField(default=999, verbose_name='类别排序')),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100, verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=500, verbose_name='评论内容')),
                ('comment_date', models.DateTimeField(verbose_name='评论日期')),
                ('comment_user', models.CharField(max_length=30, verbose_name='评论人')),
                ('book_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cs_pdf.book', verbose_name='评论所属书名')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='book_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cs_pdf.category', verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_tags',
            field=models.ManyToManyField(blank=True, to='cs_pdf.Tag', verbose_name='标签'),
        ),
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TblAbout(models.Model):
    about_id = models.AutoField(primary_key=True)
    about_datetime = models.DateTimeField(blank=True, null=True)
    about_pics = models.CharField(max_length=255, blank=True, null=True)
    about_content = models.CharField(max_length=255, blank=True, null=True)
    about_content_description = models.TextField(blank=True, null=True)
    about_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_about'


class TblAboutExpert(models.Model):
    expert_id = models.AutoField(primary_key=True)
    expert_datetime = models.DateTimeField(blank=True, null=True)
    expert_name = models.CharField(max_length=255, blank=True, null=True)
    expert_skill = models.CharField(max_length=255, blank=True, null=True)
    expert_avtar = models.CharField(max_length=255, blank=True, null=True)
    expert_description = models.TextField(blank=True, null=True)
    expert_details_added_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='expert_details_added_by')
    expert_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_about_expert'


class TblBlog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_datetime = models.DateTimeField(blank=True, null=True)
    blog_title = models.CharField(max_length=255, blank=True, null=True)
    blog_summary = models.CharField(max_length=255, blank=True, null=True)
    blog_content = models.TextField(blank=True, null=True)
    blog_like = models.IntegerField(db_column='blog_Like', blank=True, null=True)  # Field name made lowercase.
    blog_description = models.TextField(blank=True, null=True)
    blog_added_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='blog_added_by')
    blog_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)
    blog_keyword = models.CharField(max_length=255, blank=True, null=True)
    blog_pics = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_blog'


class TblBlogComments(models.Model):
    blog_comments_id = models.AutoField(primary_key=True)
    blog_comments_datetime = models.DateTimeField(blank=True, null=True)
    blog = models.ForeignKey(TblBlog, models.DO_NOTHING)
    blog_comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_blog_comments'


class TblBlogGvp(models.Model):
    blog_gvp_id = models.AutoField(primary_key=True)
    blog_gvp_datetime = models.DateTimeField(blank=True, null=True)
    blog = models.ForeignKey(TblBlog, models.DO_NOTHING)
    blog_gif = models.CharField(max_length=255, blank=True, null=True)
    blog_video = models.CharField(max_length=255, blank=True, null=True)
    blog_pics = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_blog_gvp'


class TblHome(models.Model):
    home_id = models.AutoField(primary_key=True)
    home_datetime = models.DateTimeField(blank=True, null=True)
    home_pics = models.CharField(max_length=255, blank=True, null=True)
    home_content = models.CharField(max_length=255, blank=True, null=True)
    home_content_description = models.TextField(blank=True, null=True)
    home_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_home'


class TblLearnData(models.Model):
    learn_data_id = models.AutoField(primary_key=True)
    learn_data_datetime = models.DateTimeField(blank=True, null=True)
    learn_topics = models.ForeignKey('TblLearnTopics', models.DO_NOTHING)
    learn_data_like = models.IntegerField(db_column='learn_data_Like', blank=True, null=True)  # Field name made lowercase.
    learn_data_icon = models.CharField(max_length=255, blank=True, null=True)
    learn_data = models.CharField(max_length=255, blank=True, null=True)
    learn_data_description = models.TextField(blank=True, null=True)
    learn_data_added_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='learn_data_added_by')
    learn_data_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)
    learn_data_keyword = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_learn_data'


class TblLearnDataComments(models.Model):
    learn_data_comments_id = models.AutoField(primary_key=True)
    learn_data_comments_datetime = models.DateTimeField(blank=True, null=True)
    learn_data = models.ForeignKey(TblLearnData, models.DO_NOTHING)
    learn_data_comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_learn_data_comments'


class TblLearnDataGvp(models.Model):
    learn_data_gvp_id = models.AutoField(primary_key=True)
    learn_data_gvp_datetime = models.DateTimeField(blank=True, null=True)
    learn_data = models.ForeignKey(TblLearnData, models.DO_NOTHING)
    learn_data_gif = models.CharField(max_length=255, blank=True, null=True)
    learn_data_video = models.CharField(max_length=255, blank=True, null=True)
    learn_data_pics = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_learn_data_gvp'


class TblLearnTopics(models.Model):
    learn_topics_id = models.AutoField(primary_key=True)
    learn_topics_datetime = models.DateTimeField(blank=True, null=True)
    learn_topics = models.CharField(max_length=255, blank=True, null=True)
    learn_topics_icon = models.CharField(max_length=255, blank=True, null=True)
    learn_topics_coverpage_img = models.CharField(max_length=255, blank=True, null=True)
    learn_topics_description = models.TextField(blank=True, null=True)
    learn_topics_added_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='learn_topics_added_by')
    learn_topics_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_learn_topics'


class TblPublish(models.Model):
    publish_id = models.AutoField(primary_key=True)
    input = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_publish'


class TblSnippetData(models.Model):
    snippet_data_id = models.AutoField(primary_key=True)
    snippet_data_datetime = models.DateTimeField(blank=True, null=True)
    snippet_topics = models.ForeignKey('TblSnippetTopics', models.DO_NOTHING)
    snippet_data_like = models.IntegerField(db_column='snippet_data_Like', blank=True, null=True)  # Field name made lowercase.
    snippet_data_icon = models.CharField(max_length=255, blank=True, null=True)
    snippet_data_description = models.TextField(blank=True, null=True)
    snippet_data_expire = models.CharField(max_length=100, blank=True, null=True)
    snippet_data_added_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='snippet_data_added_by')
    snippet_data_publish = models.ForeignKey(TblPublish, models.DO_NOTHING)
    snippet_data = models.TextField(blank=True, null=True)
    snippet_data_subject = models.CharField(max_length=255, blank=True, null=True)
    snippet_data_keyword = models.CharField(max_length=255, blank=True, null=True)
    snippet_data_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_snippet_data'


class TblSnippetDataGvp(models.Model):
    snippet_data_gvp_id = models.AutoField(primary_key=True)
    snippet_data_gvp_datetime = models.DateTimeField(blank=True, null=True)
    snippet_data = models.ForeignKey(TblSnippetData, models.DO_NOTHING)
    snippet_data_gif = models.CharField(max_length=255, blank=True, null=True)
    snippet_data_video = models.CharField(max_length=255, blank=True, null=True)
    snippet_data_pics = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_snippet_data_gvp'


class TblSnippetTopics(models.Model):
    snippet_topics_id = models.AutoField(primary_key=True)
    snippet_topics_datetime = models.DateTimeField(blank=True, null=True)
    snippet_topics = models.CharField(max_length=100, blank=True, null=True)
    snippet_topics_icon = models.CharField(max_length=255, blank=True, null=True)
    snippet_topics_coverpage_img = models.CharField(max_length=255, blank=True, null=True)
    snippet_topics_description = models.TextField(blank=True, null=True)
    snippet_topics_expire = models.CharField(max_length=100, blank=True, null=True)
    snippet_topics_added_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='Snippet_topics_added_by')  # Field name made lowercase.
    snippet_topics_publish = models.ForeignKey(TblPublish, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_snippet_topics'

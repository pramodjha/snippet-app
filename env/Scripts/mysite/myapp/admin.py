from django.contrib import admin
from django import forms
from .models import TblPublish, TblSnippetTopics, TblSnippetData, TblLearnTopics, TblLearnData, TblBlog, TblBlogComments, TblLearnDataComments, TblBlogGvp, TblLearnDataGvp, TblSnippetDataGvp, TblHome, TblAbout
from django.contrib.auth.models import User
from .form import TblLearnTopicsForm

#@admin.register(TblAbout)
class TblAboutAdmin(admin.ModelAdmin):
    list_display = ('about_id','about_datetime', 'about_content','about_content_description','about_pics','about_publish')
    fields = ['about_content','about_content_description','about_pics','about_publish']
admin.site.register(TblAbout,TblAboutAdmin)

class TblPublishAdmin(admin.ModelAdmin):
    list_display = ('publish_id','input')
    search_fields = ['publish_id']
admin.site.register(TblPublish,TblPublishAdmin)

class TblLearnTopicsAdmin(admin.ModelAdmin):
    form = TblLearnTopicsForm
    list_display = ('learn_topics_id','learn_topics_datetime','learn_topics','learn_topics_icon','learn_topics_coverpage_img','learn_topics_coverpage_img','learn_topics_added_by','learn_topics_publish_id')
    search_fields = ['learn_topics_id']
    readonly_fields = ('learn_topics_added_by',)
    def save_model(self, request, obj, form, change):
        obj.learn_topics_added_by = request.user
        obj.save()
admin.site.register(TblLearnTopics,TblLearnTopicsAdmin)

class TblSnippetTopicsAdmin(admin.ModelAdmin):
    list_display = ('snippet_topics_id','snippet_topics','snippet_topics_icon','snippet_topics_coverpage_img','snippet_topics_coverpage_img','snippet_topics_added_by','snippet_topics_publish_id')
    search_fields = ['snippet_topics_id']
    readonly_fields = ('snippet_topics_added_by',)
    def save_model(self, request, obj, form, change):
        obj.snippet_topics_added_by = request.user
        obj.save()
admin.site.register(TblSnippetTopics,TblSnippetTopicsAdmin)

class TblSnippetDataAdmin(admin.ModelAdmin):
    list_display = ('snippet_data_id','snippet_data_datetime','snippet_topics_id','snippet_data_like','snippet_data_icon','snippet_data','snippet_data_description','snippet_data_added_by','snippet_data_publish_id')
    search_fields = ['snippet_data_id']
admin.site.register(TblSnippetData,TblSnippetDataAdmin)


class TblLearnDataAdmin(admin.ModelAdmin):
    list_display = ('learn_data_id','learn_data_datetime','learn_topics_id','learn_data_like','learn_data_icon','learn_data','learn_data_description','learn_data_added_by','learn_data_publish_id')
    search_fields = ['learn_data_id']
admin.site.register(TblLearnData,TblLearnDataAdmin)


admin.site.register(TblBlog)

class TblBlogCommentsAdmin(admin.ModelAdmin):
    list_display = ('blog_comments_id','blog_id','blog_comments')
    search_fields = ['blog_comments_id']
admin.site.register(TblBlogComments,TblBlogCommentsAdmin)

admin.site.register(TblLearnDataComments)
admin.site.register(TblBlogGvp)
admin.site.register(TblLearnDataGvp)
admin.site.register(TblSnippetDataGvp)
admin.site.register(TblHome)

#class TblAboutAdmin(admin.ModelAdmin):
#    list_display = ('about_id','about_datetime','about_pics','about_content','about_content_description')
#    search_fields = ['about_id']
#admin.site.register(TblAbout,TblAboutAdmin)

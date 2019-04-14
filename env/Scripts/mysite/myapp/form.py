from django import forms
from django.contrib.auth.models import User
from .models import TblPublish , TblSnippetTopics, TblSnippetData, TblLearnTopics, TblLearnData, TblBlog, TblBlogComments,TblLearnDataComments, TblBlogGvp, TblLearnDataGvp,TblSnippetDataGvp, TblHome, TblAbout

class TblPublishForm(forms.ModelForm):
    class Meta():
        model = TblPublish
        fields = '__all__'

class TblSnippetTopicsForm(forms.ModelForm):
    class Meta():
        model = TblSnippetTopics
        fields = '__all__'

class TblSnippetDataForm(forms.ModelForm):
    class Meta():
        model = TblSnippetData
        fields = ['snippet_topics','snippet_data_subject','snippet_data_description','snippet_data_keyword','snippet_data_code','snippet_data_datetime','snippet_data_added_by','snippet_topics','snippet_data_publish']
        def clean_snippet_topics_added_by(self):
            if not self.cleaned_data['snippet_topics_added_by']:
                return User()
            return self.cleaned_data['snippet_topics_added_by']

    def __init__(self, *args, **kwargs):
        super(TblSnippetDataForm, self).__init__(*args, **kwargs)
        self.fields['snippet_data_datetime'].widget = forms.HiddenInput()
        self.fields['snippet_data_added_by'].widget = forms.HiddenInput()
        self.fields['snippet_topics'].widget = forms.HiddenInput()
        self.fields['snippet_data_subject'].label = "Title/Topics"
        self.fields['snippet_data_description'].label = "Brief Description"
        self.fields['snippet_data_keyword'].label = "Keyword For Search"
        self.fields['snippet_data_code'].label = "Snippet (Code)"
        self.fields['snippet_data_publish'].label = "Ready-To-Publish"

class TblBlogForm(forms.ModelForm):
    class Meta():
        model = TblBlog
        fields = ['blog_pics','blog_title','blog_description','blog_content','blog_keyword','blog_publish','blog_datetime','blog_summary','blog_like','blog_added_by']

    def __init__(self, *args, **kwargs):
        super(TblBlogForm, self).__init__(*args, **kwargs)
        self.fields['blog_datetime'].widget = forms.HiddenInput()
        self.fields['blog_summary'].widget = forms.HiddenInput()
        self.fields['blog_like'].widget = forms.HiddenInput()
        self.fields['blog_added_by'].widget = forms.HiddenInput()
        self.fields['blog_title'].label = "Title/Topics"
        self.fields['blog_description'].label = "Brief Description"
        self.fields['blog_content'].label = "Blog Content"
        self.fields['blog_keyword'].label = "Keyword For Search"
        self.fields['blog_publish'].label = "Ready-To-Publish"
        self.fields['blog_pics'].label = "Upload Pics"



class TblBlogCommentsForm(forms.ModelForm):
    class Meta():
        model = TblBlogComments
        fields = '__all__'

class TblLearnDataForm(forms.ModelForm):
    class Meta():
        model = TblLearnData
        fields = ['learn_data','learn_data_description','learn_data_keyword','learn_data_publish','learn_data_datetime','learn_data_added_by','learn_topics','learn_data_like','learn_data_icon']

    def __init__(self, *args, **kwargs):
        super(TblLearnDataForm, self).__init__(*args, **kwargs)
        self.fields['learn_data_datetime'].widget = forms.HiddenInput()
        self.fields['learn_data_added_by'].widget = forms.HiddenInput()
        self.fields['learn_topics'].widget = forms.HiddenInput()
        self.fields['learn_data_like'].widget = forms.HiddenInput()
        self.fields['learn_data_icon'].widget = forms.HiddenInput()
        self.fields['learn_data'].label = "Title/Topics"
        self.fields['learn_data_description'].label = "Brief Description"
        self.fields['learn_data_keyword'].label = "Keyword For Search"
        self.fields['learn_data_publish'].label = "Ready-To-Publish"

class TblLearnDataCommentsForm(forms.ModelForm):
    class Meta():
        model = TblLearnDataComments
        fields = '__all__'
class TblBlogGvpForm(forms.ModelForm):
    class Meta():
        model = TblBlogGvp
        fields = '__all__'
class TblLearnDataGvpForm(forms.ModelForm):
    class Meta():
        model = TblLearnDataGvp
        fields = '__all__'
class TblHomeForm(forms.ModelForm):
    class Meta():
        model = TblHome
        fields = '__all__'
class TblAboutForm(forms.ModelForm):
    class Meta():
        model = TblAbout
        fields = '__all__'

class TblLearnTopicsForm(forms.ModelForm):
    class Meta():
        model = TblLearnTopics
        fields = '__all__'

    def clean_learn_topics_added_by(self):
        if not self.cleaned_data['learn_topics_added_by']:
            return User()
        return self.cleaned_data['learn_topics_added_by']

class TblSnippetTopicsForm(forms.ModelForm):
    class Meta():
        model = TblSnippetTopics
        fields = '__all__'

    def clean_snippet_topics_added_by(self):
        if not self.cleaned_data['snippet_topics_added_by']:
            return User()
        return self.cleaned_data['snippet_topics_added_by']

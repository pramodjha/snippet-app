from django import forms
from django.contrib.auth.models import User
from .models import TblPublish , TblSnippetTopics, TblSnippetData, TblLearnTopics, TblLearnData, TblBlog, TblBlogComments,TblLearnDataComments, TblBlogGvp, TblLearnDataGvp,TblSnippetDataGvp, TblHome, TblAbout

class UsersigninForm(forms.Form):
    username = forms.CharField(required = True, label = 'Username', max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required = True, label = 'Password', max_length = 32, widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserRegistrationForm(forms.Form):
    username = forms.CharField(required = True, min_length=6,label = 'Username', max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Username'}) )
    email = forms.EmailField(required = True, label = 'Email', max_length = 100, widget=forms.EmailInput(attrs={'placeholder': 'e.g. : email@gmail.com'}))
    firstname = forms.CharField(required = True, label = 'First Name', max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(required = True, label = 'Last Name', max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(required = True, label = 'Password', max_length = 100, widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))
    passwordagain = forms.CharField(required = True, label = 'Password (Again)', max_length = 100, widget = forms.PasswordInput(attrs={'placeholder': 'Password (Again)'}))

class TblPublishForm(forms.ModelForm):
    class Meta():
        model = TblPublish
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
        self.fields['snippet_data_subject'].widget.attrs['placeholder'] = "Title/Topics"
        self.fields['snippet_data_description'].widget.attrs['placeholder'] = "Brief Description"
        self.fields['snippet_data_keyword'].widget.attrs['placeholder'] ="Keyword For Search"
        self.fields['snippet_data_code'].widget.attrs['placeholder'] = "Snippet (Code)"
        self.fields['snippet_data_publish'].widget.attrs['placeholder'] = "Ready-To-Publish"
        self.fields['snippet_data_publish'].label = "Publish"

class TblBlogForm(forms.ModelForm):
    class Meta():
        model = TblBlog
        fields = ['blog_title','blog_description','blog_keyword','blog_content','blog_pics','blog_publish','blog_datetime','blog_summary','blog_like','blog_added_by']

    def __init__(self, *args, **kwargs):
        super(TblBlogForm, self).__init__(*args, **kwargs)
        self.fields['blog_datetime'].widget = forms.HiddenInput()
        self.fields['blog_summary'].widget = forms.HiddenInput()
        self.fields['blog_like'].widget = forms.HiddenInput()
        self.fields['blog_added_by'].widget = forms.HiddenInput()
        self.fields['blog_title'].widget.attrs['placeholder'] = "Title/Topics"
        self.fields['blog_description'].widget.attrs['placeholder'] = "Brief Description"
        self.fields['blog_content'].widget.attrs['placeholder'] = "Blog Content"
        self.fields['blog_keyword'].widget.attrs['placeholder'] = "Keyword For Search"
        self.fields['blog_pics'].widget.attrs['placeholder'] = "Upload Pics"
        self.fields['blog_publish'].label = "Publish"



class TblBlogCommentsForm(forms.ModelForm):
    class Meta():
        model = TblBlogComments
        fields = '__all__'

class TblLearnDataForm(forms.ModelForm):
    class Meta():
        model = TblLearnData
        fields = ['learn_data','learn_data_keyword','learn_data_description','learn_data_publish','learn_data_datetime','learn_data_added_by','learn_topics','learn_data_like','learn_data_icon']

    def __init__(self, *args, **kwargs):
        super(TblLearnDataForm, self).__init__(*args, **kwargs)
        self.fields['learn_data_datetime'].widget = forms.HiddenInput()
        self.fields['learn_data_added_by'].widget = forms.HiddenInput()
        self.fields['learn_topics'].widget = forms.HiddenInput()
        self.fields['learn_data_like'].widget = forms.HiddenInput()
        self.fields['learn_data_icon'].widget = forms.HiddenInput()
        self.fields['learn_data'].widget.attrs['placeholder'] = "Title/Topics"
        self.fields['learn_data_description'].widget.attrs['placeholder'] = "Brief Description"
        self.fields['learn_data_keyword'].widget.attrs['placeholder'] = "Keyword For Search"
        self.fields['learn_data_publish'].label = "Publish"

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

    def __init__(self, *args, **kwargs):
        super(TblHomeForm, self).__init__(*args, **kwargs)
        self.fields['home_datetime'].widget = forms.HiddenInput()
        self.fields['home_added_by'].widget = forms.HiddenInput()
        self.fields['home_pics'].widget.attrs['placeholder'] = "Upload Image"
        self.fields['home_content'].widget.attrs['placeholder'] = "Content"
        self.fields['home_content_description'].widget.attrs['placeholder'] = "Description"
        self.fields['home_publish'].label = "Publish"


class TblAboutForm(forms.ModelForm):
    class Meta():
        model = TblAbout
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(TblAboutForm, self).__init__(*args, **kwargs)
        self.fields['about_datetime'].widget = forms.HiddenInput()
        self.fields['about_added_by'].widget = forms.HiddenInput()
        self.fields['about_pics'].widget.attrs['placeholder'] = "Upload Image"
        self.fields['about_content'].widget.attrs['placeholder'] = "Content"
        self.fields['about_content_description'].widget.attrs['placeholder'] = "Description"
        self.fields['about_publish'].label = "Publish"

class TblLearnTopicsForm(forms.ModelForm):
    class Meta():
        model = TblLearnTopics
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(TblLearnTopicsForm, self).__init__(*args, **kwargs)
        self.fields['learn_topics_datetime'].widget = forms.HiddenInput()
        self.fields['learn_topics_added_by'].widget = forms.HiddenInput()
        self.fields['learn_topics_icon'].widget = forms.HiddenInput()
        self.fields['learn_topics_coverpage_img'].widget = forms.HiddenInput()
        self.fields['learn_topics'].widget.attrs['placeholder'] = "Topics"
        self.fields['learn_topics_description'].widget.attrs['placeholder']  = "Description"
        self.fields['learn_topics_publish'].label = "Publish"



    def clean_learn_topics_added_by(self):
        if not self.cleaned_data['learn_topics_added_by']:
            return User()
        return self.cleaned_data['learn_topics_added_by']

class TblSnippetTopicsForm(forms.ModelForm):
    class Meta():
        model = TblSnippetTopics
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(TblSnippetTopicsForm, self).__init__(*args, **kwargs)
        self.fields['snippet_topics_datetime'].widget = forms.HiddenInput()
        self.fields['snippet_topics_added_by'].widget = forms.HiddenInput()
        self.fields['snippet_topics_icon'].widget = forms.HiddenInput()
        self.fields['snippet_topics_coverpage_img'].widget = forms.HiddenInput()
        self.fields['snippet_topics_expire'].widget = forms.HiddenInput()
        self.fields['snippet_topics'].widget.attrs['placeholder'] = "Topics"
        self.fields['snippet_topics_description'].widget.attrs['placeholder']  = "Description"
        self.fields['snippet_topics_publish'].label = "Publish"

    def clean_snippet_topics_added_by(self):
        if not self.cleaned_data['snippet_topics_added_by']:
            return User()
        return self.cleaned_data['snippet_topics_added_by']

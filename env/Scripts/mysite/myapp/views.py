from .models import TblPublish, TblSnippetTopics, TblSnippetData, TblLearnTopics, TblLearnData, TblBlog, TblBlogComments, TblLearnDataComments, TblBlogGvp, TblLearnDataGvp, TblSnippetDataGvp, TblAbout, TblHome, TblQueries, TblSnippetLike,TblLearnLike
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
import sys
from .form import TblAboutForm, TblSnippetTopicsForm, TblSnippetDataForm ,TblBlogForm,TblBlogCommentsForm, TblLearnDataCommentsForm, TblBlogGvpForm,TblLearnDataGvpForm,TblHomeForm,TblAboutForm, TblLearnDataForm, UsersigninForm, UserRegistrationForm, TblLearnTopicsForm, TblQueriesForm,SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .filters import SnippetFilter, LearnFilter, BlogFilter
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.
@login_required
def email(request):
    print("Email")
    subject = 'Thank you for registering to our site'
    current_site = get_current_site(request)
    message = render_to_string('myapp/acc_active_email.html', {
                'user': User,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(User.pk)).decode(),
                'token':account_activation_token.make_token(User),
            })
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['jha.pramod234@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect(reverse('home'))

def activate(request, uidb64, token):
    redirect_url = 'thankyou'
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        print(user)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return  HttpResponseRedirect(reverse(redirect_url,args = (2,)))
    else:
        return HttpResponse('Activation link is invalid!')

def template_generator(template_folder='myapp',function_name=None,file_extention='.html'):
    template = template_folder + "/" +function_name + file_extention
    activetab = function_name
    return template, activetab

def get_function_name():
    function_name = sys._getframe(1).f_code.co_name
    return function_name

def signin(request):
    template = 'myapp/dynamic_form.html'
    activetab = 'signin'
    redirect_url1 = 'signin'
    action = 'Enter your Credential'
    condition = 3
    form = UsersigninForm()
    if request.method == 'POST':
        form =  UsersigninForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username =  userObj['username']
            password =  userObj['password']
            if (User.objects.filter(username=username).exists()):
                user = User.objects.get(username = username)
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
    context = {'form' : form,'activetab':activetab,'redirect_url1':redirect_url1,'action':action,'condition':condition}
    return render(request, template,context)


def signup(request):
    template = 'myapp/dynamic_form.html'
    activetab = 'signup'
    redirect_url1 = 'signup'
    action = 'Create Account'
    condition = 3
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('myapp/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            email_from = settings.EMAIL_HOST_USER
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, email_from,to=[to_email]
            )
            email.send()
            return  HttpResponseRedirect(reverse('thankyou',args = (1,)))
    context = {'form' : form,'activetab':activetab,'redirect_url1':redirect_url1,'action':action,'condition':condition}
    return render(request, template,context)


def signout(request):
    request.session.delete()
    logout(request)
    return HttpResponseRedirect(reverse('signin'))


def home(request):
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    username = request.user
    model = TblHome.objects.filter(home_publish__in=[2])
    context = {'activetab':activetab,'model':model,'username':username}
    return render(request, template,context)

@login_required
def home_add_form(request):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username
    template = 'myapp/dynamic_form.html'
    activetab = 'home'
    action = 'Add'
    redirect_url1 = 'home'
    redirect_url2 = 'homeaddform'
    condition = 1
    form = TblHomeForm(initial={'home_added_by':userid})
    if request.method == 'POST':
        form = TblHomeForm(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url2':redirect_url2,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)

@login_required
def home_edit_form(request,home_id):
    template = 'myapp/dynamic_form.html'
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username
    e = TblHome.objects.get(home_id=home_id)
    homeid = TblHome.objects.get(home_id=home_id).home_id
    model1 = TblHome.objects.get(home_id__in=[home_id]).home_content
    userid = User.objects.get(username=request.user).id
    condition = 2
    activetab = 'home'
    action = 'Edit'
    redirect_url1 = 'home'
    redirect_url2 = 'homeeditform'
    form = TblHomeForm(instance=e)
    if request.method == 'POST':
        form = TblHomeForm(request.POST,request.FILES,instance=e)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'id':homeid,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'model1':model1,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)


def about(request):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    model = TblAbout.objects.filter(about_publish__in=[2])
    context = {'activetab':activetab,'model':model,'username':username}
    return render(request, template,context)



@login_required
def about_add_form(request):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username
    template = 'myapp/dynamic_form.html'
    activetab = 'about'
    action = 'Add'
    redirect_url1 = 'about'
    redirect_url2 = 'aboutaddform'
    condition = 1
    form = TblAboutForm(initial={'about_added_by':userid})
    if request.method == 'POST':
        form = TblAboutForm(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url2':redirect_url2,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)

@login_required
def about_edit_form(request,slug):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    e = TblAbout.objects.get(slug=slug)
    aboutid = TblAbout.objects.get(slug=slug).about_id
    model1 = TblAbout.objects.get(slug__in=[slug]).about_content
    userid = User.objects.get(username=request.user).id
    condition = 2
    activetab = 'about'
    action = 'Edit'
    redirect_url1 = 'about'
    redirect_url2 = 'abouteditform'
    form = TblAboutForm(instance=e)
    if request.method == 'POST':
        form = TblAboutForm(request.POST,request.FILES,instance=e)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'id':aboutid,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'model1':model1,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)


def snippet(request):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    model = TblSnippetTopics.objects.filter(snippet_topics_publish__in=[2])
    context = {'activetab':activetab,'model':model,'username':username}
    return render(request, template,context)

@login_required
def snippet_add_form(request):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username
    template = 'myapp/dynamic_form.html'
    activetab = 'snippet'
    action = 'Add'
    redirect_url1 = 'snippet'
    redirect_url2 = 'snippetaddform'
    condition = 1
    form = TblSnippetTopicsForm(initial={'snippet_topics_added_by':userid})
    if request.method == 'POST':
        form = TblSnippetTopicsForm(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url2':redirect_url2,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)

@login_required
def snippet_edit_form(request,slug):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    e = TblSnippetTopics.objects.get(slug=slug)
    aboutid = TblSnippetTopics.objects.get(slug=slug).snippet_topics_id
    model1 = TblSnippetTopics.objects.get(slug=slug).snippet_topics
    userid = User.objects.get(username=request.user).id
    condition = 2
    activetab = 'snippet'
    action = 'Edit'
    redirect_url1 = 'snippet'
    redirect_url2 = 'snippeteditform'
    form = TblSnippetTopicsForm(instance=e)
    if request.method == 'POST':
        form = TblSnippetTopicsForm(request.POST,request.FILES,instance=e)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'id':aboutid,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'model1':model1,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)

def snippet_topics(request,slug):
    username = request.user
    function_name = get_function_name()
    snippet_topics_id = TblSnippetTopics.objects.get(slug=slug).snippet_topics_id
    template, activetab = template_generator(function_name=function_name)
    model = TblSnippetData.objects.filter(snippet_data_publish__in=[2]).filter(snippet_topics__in=[snippet_topics_id])
    model1 = TblSnippetTopics.objects.filter(snippet_topics_id__in=[snippet_topics_id])
    model2 = TblSnippetLike.objects.filter(snippet_like__in=[1])
    heading = 'About/Add'
    activetab = 'snippet'
    snippet_list = TblSnippetData.objects.filter(snippet_topics__in=[snippet_topics_id])
    snippet_filter = SnippetFilter(request.GET, queryset=snippet_list)
    context = {'activetab':activetab,'model':model,'model1':model1,'heading':heading,'filter': snippet_filter,'username':username,'model2':model2}
    return render(request, template,context)


@login_required
def snippet_like(request):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username
    redirect_url1 = 'snippet'
    print(username)
    if request.method == 'POST':
        slug = request.POST.get('slug')
        print(slug)
        snippetid = TblSnippetData.objects.get(slug=slug)
        try:
            instance = TblSnippetLike.objects.get(user_liked=userid)
            print(instance.snippet_like == True)
            if instance.snippet_like == True:
                instance.snippet_like = False
                instance.save()
            else:
                instance.snippet_like = True
                instance.save()
        except:
            user_instance = User.objects.get(id=userid)
            p = TblSnippetLike.objects.create(snippet_data_id=snippetid, user_liked=user_instance,snippet_like=True)
        #print(slug)
        return HttpResponseRedirect(reverse(redirect_url1))
    return HttpResponseRedirect(reverse(redirect_url1))

@login_required
def snippet_topics_add_form(request,slug):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    model1 = TblSnippetTopics.objects.get(slug__in=[slug]).snippet_topics
    snippet_topics_id = TblSnippetTopics.objects.get(slug__in=[slug]).snippet_topics_id
    model = TblSnippetData.objects.filter(snippet_data_publish__in=[2]).filter(snippet_topics__in=[snippet_topics_id])
    userid = User.objects.get(username=request.user).id
    activetab = 'snippet'
    action = 'Add'
    redirect_url1 = 'snippet'
    redirect_url2 = 'snippettopics'
    redirect_url3 = 'snippettopicsaddform'
    form = TblSnippetDataForm(initial={'snippet_topics':snippet_topics_id,'snippet_data_added_by':userid})
    if request.method == 'POST':
        form = TblSnippetDataForm(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url2,args = (slug,)))
    context = {'form':form,'id':slug,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url3':redirect_url3,'model1':model1,'activetab':activetab,'model1':model1,'action':action,'username':username}
    return render(request, template,context)

@login_required
def snippet_topics_edit_form(request,slug):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    e = TblSnippetData.objects.get(slug=slug)
    topicid = TblSnippetData.objects.get(slug=slug).snippet_topics
    topics_slug = TblSnippetTopics.objects.get(snippet_topics=topicid).slug
    activetab = 'snippet'
    action = 'Edit'
    redirect_url1 = 'snippet'
    redirect_url2 = 'snippettopics'
    redirect_url3 = 'snippettopicseditform'
    form = TblSnippetDataForm(instance=e)
    if request.method == 'POST':
        form = TblSnippetDataForm(request.POST,request.FILES,instance=e)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url2,args = (topics_slug,)))
    context = {'form':form,'id':topics_slug,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url3':redirect_url3,'activetab':activetab,'model1':topicid,'action':action,'username':username}
    return render(request, template,context)

def snippet_topics_view(request,slug):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    activetab = 'snippet'
    redirect_url = slug
    model = TblSnippetData.objects.filter(slug__in=[slug])
    topics = TblSnippetData.objects.get(slug=slug).snippet_topics
    topics_slug = TblSnippetTopics.objects.get(snippet_topics=topics).slug
    snippet_title = TblSnippetData.objects.get(slug=slug).snippet_data_subject
    context = {'model':model,'activetab':activetab,'topics_slug':topics_slug,'snippet_title':snippet_title,'username':username}
    return render(request, template,context)

def learn(request):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    model = TblLearnTopics.objects.filter(learn_topics_publish__in=[2])
    context = {'activetab':activetab,'model':model,'username':username}
    return render(request, template,context)


@login_required
def learn_add_form(request):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username
    template = 'myapp/dynamic_form.html'
    activetab = 'learn'
    action = 'Add'
    redirect_url1 = 'learn'
    redirect_url2 = 'learnaddform'
    condition = 1
    form = TblLearnTopicsForm(initial={'learn_topics_added_by':userid})
    if request.method == 'POST':
        form = TblLearnTopicsForm(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url2':redirect_url2,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)

@login_required
def learn_edit_form(request,slug):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    model1 = TblLearnTopics.objects.get(slug=slug).learn_topics
    learn_data_id = TblLearnTopics.objects.get(slug=slug).learn_topics_id
    e = TblLearnTopics.objects.get(learn_topics_id=learn_data_id)
    aboutid = TblLearnTopics.objects.get(learn_topics_id=learn_data_id).learn_topics_id
    condition = 2
    activetab = 'learn'
    action = 'Edit'
    redirect_url1 = 'learn'
    redirect_url2 = 'learneditform'
    form = TblLearnTopicsForm(instance=e)
    if request.method == 'POST':
        form = TblLearnTopicsForm(request.POST,request.FILES,instance=e)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'id':aboutid,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'model1':model1,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)



def learn_topics(request,slug):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    model1 = TblLearnTopics.objects.filter(slug__in=[slug])
    learn_topics_id = TblLearnTopics.objects.get(slug__in=[slug]).learn_topics_id
    model = TblLearnData.objects.filter(learn_data_publish__in=[2]).filter(learn_topics__in=[learn_topics_id])
    heading = 'About/Add'
    activetab = 'learn'
    learn_list = TblLearnData.objects.filter(learn_topics__in=[learn_topics_id])
    learn_filter = LearnFilter(request.GET, queryset=learn_list)
    context = {'activetab':activetab,'model':model,'model1':model1,'heading':heading,'filter': learn_filter,'username':username}
    return render(request, template,context)

@login_required
def learn_topics_add_form(request,slug):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    model1 = TblLearnTopics.objects.get(slug__in=[slug]).learn_topics
    learn_topics_id = TblLearnTopics.objects.get(slug__in=[slug]).learn_topics_id
    model = TblLearnData.objects.filter(learn_data_publish__in=[2]).filter(learn_topics__in=[learn_topics_id])
    activetab = 'learn'
    action = 'Add'
    redirect_url1 = 'learn'
    redirect_url2 = 'learntopics'
    redirect_url3 = 'learntopicsaddform'
    form = TblLearnDataForm(initial={'learn_topics':learn_topics_id,'learn_data_added_by':userid})
    if request.method == 'POST':
        form = TblLearnDataForm(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url2,args = (slug,)))
    context = {'form':form,'id':slug,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url3':redirect_url3,'model1':model1,'activetab':activetab,'model1':model1,'action':action,'username':username}
    return render(request, template,context)

@login_required
def learn_topics_edit_form(request,slug):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    e = TblLearnData.objects.get(slug=slug)
    learnid = TblLearnData.objects.get(slug=slug).learn_topics_id
    model1 = TblLearnTopics.objects.get(learn_topics_id__in=[learnid]).learn_topics
    topics_slug = TblLearnTopics.objects.get(learn_topics_id__in=[learnid]).slug
    activetab = 'learn'
    action = 'Edit'
    redirect_url1 = 'learn'
    redirect_url2 = 'learntopics'
    redirect_url3 = 'learntopicseditform'
    form = TblLearnDataForm(instance=e)
    if request.method == 'POST':
        form = TblLearnDataForm(request.POST,request.FILES,instance=e)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url2,args = (topics_slug,)))
    context = {'form':form,'id':learnid,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url3':redirect_url3,'model1':model1,'activetab':activetab,'model1':model1,'action':action,'username':username}
    return render(request, template,context)

def learn_topics_view(request,slug):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    activetab = 'learn'
    model = TblLearnData.objects.filter(slug__in=[slug])
    topics = TblLearnData.objects.get(slug=slug).learn_topics
    topics_slug = TblLearnTopics.objects.get(learn_topics=topics).slug
    learn_title = TblLearnData.objects.get(slug=slug).learn_data
    context = {'model':model,'activetab':activetab,'topics_slug':topics_slug,'learn_title':learn_title,'username':username}
    return render(request, template,context)

def blog(request):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    model = TblBlog.objects.filter(blog_publish__in=[2])
    context = {'activetab':activetab,'model':model,'username':username}
    return render(request, template,context)


def blog_topics(request,slug):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    model = TblBlog.objects.filter(blog_publish__in=[2]).filter(slug__in=[slug])
    model1 = TblBlog.objects.filter(slug__in=[slug])
    activetab = 'blog'
    heading = "edit"
    blog_list = TblBlog.objects.filter(slug__in=[slug])
    blog_filter = BlogFilter(request.GET, queryset=blog_list)
    context = {'activetab':activetab,'id':slug,'model':model,'model1':model1,'heading':heading,'filter': blog_filter,'username':username}
    return render(request, template,context)

@login_required
def blog_topics_add_form(request):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    activetab = 'blog'
    action = 'Add'
    redirect_url1 = 'blog'
    redirect_url2 = 'blogtopicsaddform'
    condition = 1
    form = TblBlogForm(initial={'blog_added_by':userid})
    if request.method == 'POST':
        form = TblBlogForm(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return HttpResponseRedirect(reverse(redirect_url1))
    context = {'form':form,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url2':redirect_url2,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)

@login_required
def blog_topics_edit_form(request,slug):
    userdata = User.objects.all()
    userid = userdata.get(username=request.user).id
    username = userdata.get(username=request.user).username

    template = 'myapp/dynamic_form.html'
    e = TblBlog.objects.get(slug=slug)
    blogid = TblBlog.objects.get(slug=slug).blog_id
    model1 = TblBlog.objects.get(slug__in=[slug]).blog_title
    activetab = 'blog'
    action = 'Edit'
    redirect_url1 = 'blog'
    redirect_url2 = 'blogtopics'
    redirect_url3 = 'blogtopicseditform'
    form = TblBlogForm(instance=e)
    if request.method == 'POST':
        form = TblBlogForm(request.POST,request.FILES,instance=e)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            New_slug = inst.slug
            return HttpResponseRedirect(reverse(redirect_url2,args = (New_slug,)))
    context = {'form':form,'id':blogid,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url3':redirect_url3,'model1':model1,'activetab':activetab,'action':action,'username':username}
    return render(request, template,context)


def contact(request):
    username = request.user
    function_name = get_function_name()
    template, activetab = template_generator(function_name=function_name)
    model = TblQueries.objects.all()
    context = {'activetab':activetab,'model':model,'username':username}
    return render(request, template,context)

def contact_form(request):
    username = request.user
    template = 'myapp/dynamic_form.html'
    model = TblQueries.objects.all()
    activetab = 'contact'
    action = 'Add'
    redirect_url1 = 'contact'
    redirect_url2 = 'contact'
    condition = 1
    form = TblQueriesForm()
    if request.method == 'POST':
        form = TblQueriesForm(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=True)
            inst.save()
            return  HttpResponseRedirect(reverse('thankyou',args = (3,)))
    context = {'form':form,'redirect_url1':redirect_url1,'redirect_url2':redirect_url2,'redirect_url2':redirect_url2,'activetab':activetab,'action':action,'condition':condition,'username':username}
    return render(request, template,context)

def thankyou(request,ty_id):
    if ty_id =='1':
        msg = 'Please confirm your email address to complete the registration'
    elif ty_id =='2':
        msg = 'Thank you for your email confirmation. you already logged in to your account.'
    elif ty_id == '3':
        msg = 'Your Queries has been registered'
    else:
        msg = None
    template = 'myapp/thankyou.html'
    return render(request, template, {'msg':msg,'ty_id':ty_id})

def like_it(request):
    user = request.user
    if request.method == 'POST':
        ObjectId = int(request.POST['objectid'])
        Tip = str(request.POST['contentType'])

        likes = LikeModel.objects.filter(object_id=ObjectId, content_object=Tip) # in here we filtered the particular post with its id
        if likes: # if the particular post is there
            if str(user) in str(likes): # then we check the user which is us, in there
                like_obj = LikeModel.objects.get(user=user,object_id=ObjectId, content_object=Tip) #if we there and we returned this data, this part for saving data, I mean if this data is already created than we dont have to delete and create again, we just change LikeModel.liked true or false state, so that if you create like and it will never delete, it just change liked or like state
            else:
                pass

        if Tip == 'UserPost':
            post_content_type_by = UserPost.objects.all().first()

            if str(user) not in str(likes):
                like = LikeModel.objects.create(user=user, liked=True, content_object=ContentType.objects.get_for_model(Tip), object_id=ObjectId)
                like.save() # if data is created then we say 'new'
                okey = 'new'

            elif str(user) in str(likes) and like_obj.liked:
                like_obj.liked = False
                like_obj.save() # if data is already there, then we save it False
                okey = 'false'

            elif str(user) in str(likes) and like_obj.liked == False:
                like_obj.liked = True
                like_obj.save() # if data is already changed to False and we save again to True
                okey = 'true'


    return render(request,'ajaxlike.html',{'likes':likes,'okey':okey})

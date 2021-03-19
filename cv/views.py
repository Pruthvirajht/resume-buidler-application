from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm,ProfileForm,EducationForm,ExperienceForm,SkillForm
from django.contrib.auth import authenticate,login,logout
from .models import Profile,Education,Experience,Skill
from django.contrib.auth.decorators import login_required


# Home
def home(request):
    return render(request,'home.html')

#About
def about(request):
    return render(request,'about.html')

def log_out(request):
    logout(request)
    return redirect('home')

#Login
def log_in(request):   
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is  None:
            return render(request,'login.html',{'form':form,'msg':'User not Found'})
            
        else:
            login(request,user)
            return redirect('userdetail')
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})
#Signup
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =SignupForm()
    return render(request,'signup.html',{'form':form})

#USER DTEAILS
def userdetail(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).all()
        education = Education.objects.filter(user=request.user).all()
        experience = Experience.objects.filter(user=request.user).all()
        skill = Skill.objects.filter(user=request.user).all()

        return render(request,'userdetails.html',{'pf':profile,'ed':education,'ex':experience,'sk':skill})
    return render(request,'userdetails.html')

#ADD PERSONAL DETAILS
def add_persnl(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nm = request.POST['name']
            em = request.POST['email']
            ph = request.POST['phno']
            cy = request.POST['city']
            st = request.POST['state']
            ab = request.POST['about']
            ld = request.POST['linkdin']
            gh = request.POST['github']
            pf = Profile(name=nm,email=em,phno=ph,city=cy,state=st,about=ab,linkdin=ld,github=gh, user=request.user)
            pf.save()
            return redirect('userdetail')
        else:
            form = ProfileForm()
        return render(request,'addprofile.html',{'form':form})
    else:
        return redirect('login')


#EDIT PERSONAL
def edit_prsnl(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('userdetail')
    form = ProfileForm(instance=request.user.profile)
    return render(request,'addprofile.html',{'form':form})


#ADD EDUCATIONAL DETAILS
def add_edu(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sslc = request.POST['sslc']
            puc = request.POST['puc']
            degree = request.POST['degree']
            percentage = request.POST['percentage']
            city = request.POST['city']
            state = request.POST['state']
            edu = Education(sslc=sslc,puc=puc,degree=degree,percentage=percentage,city=city,state=state,user=request.user)
            edu.save()
            return redirect('userdetail')
        else:
            form = EducationForm()
            return render(request,'addeducation.html',{'form':form})
    else:
        return redirect('login')

#EDIT EDUCATIONAL DETAILS
def edit_edu(request,pk):
    edu = Education.objects.get(id=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST,instance=edu)
        if form.is_valid():
            form.save()
            return redirect('userdetail')
    form = EducationForm(instance=edu)
    return render(request,'addeducation.html',{'form':form})

#ADD EXPERIENCE DETAILS
def add_experience(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            job = request.POST['jobrole']
            cm = request.POST['companyname']
            pr = request.POST['projects']
            cy = request.POST['city']
            st = request.POST['state']
            ex = Experience(jobrole=job,companyname=cm,projects=pr,city=cy,state=st,user=request.user)
            ex.save()
            return redirect('userdetail')
        else:
            form = ExperienceForm()
            return render(request,'addexperience.html',{'form':form})
    else:
        return redirect('login')

#EDIT EXPERIENCE

def edit_experience(request,pk):
    exp = Education.objects.get(id=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST,instance=exp)
        if form.is_valid():
            form.save()
            return redirect('userdetail')
    form = ExperienceForm(instance=edu)

    return render(request,'addexperience.html',{'form':form})



#ADD SKILL

def add_skill(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sk = request.POST['skill']
            skl = Skill(skill=sk,user=request.user)
            skl.save()
            return redirect('userdetail')
        else:
            form = SkillForm()
            return render(request,'addskill.html',{'form':form})
    else:
        return redirect('login')

#EDIT SKILL

def edit_skill(request,pk):
    skill = Skill.objects.get(id=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            return redirect('userdetail')
    form = SkillForm(instance=skill)
    return render(request,'addskill.html',{'form':form})


@login_required(login_url='/login')
def selectresume(request):
    return render(request, 'selectresume.html')



@login_required(login_url='/login')
def restemp(request):
    context = {
         'pf': Profile.objects.filter(user=request.user).all(),
         'ed': Education.objects.filter(user=request.user).all(),
         'ex': Experience.objects.filter(user=request.user).all(),
         'sk': Skill.objects.filter(user=request.user).all(),
    }
    return render(request, 'restemp.html', context)


    







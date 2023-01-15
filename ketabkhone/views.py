from secrets import choice
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from platformdirs import user_cache_dir
from book.models import Book, Bookmark , Comment
from extra.models import Category, Like
from accounting.models import CustomUser
from loan.models import Debt, Loan
from .forms import Search
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
#from captcha.image import ImageCaptcha
from django.contrib.auth.models import User
# from accounting.admin import CustomUser

def bookdetail(request, book_id):
    book_obj = Book.objects.get(id=book_id)
    likes = Like.objects.filter(book_id=book_id, vote=True).count()
    try:       
        customuser = CustomUser.objects.get(user=request.user)  
        val_comment = Comment.objects.get(user=customuser, book=book_obj)
        if val_comment:
            can_comment = False
        else:
            can_comment = True

    except Exception as e:
        print('=============')
        print(e)
        val_comment = None
        can_comment = True

    print(can_comment)
    comments = Comment.objects.filter(book=book_obj)
    dislikes = Like.objects.filter(book_id=book_id, vote=False).count()
    return render(request, 'bookdetail.html', {'book_obj': book_obj,
                                               'likes': likes,
                                                "dislike": dislikes,
                                                "comments":comments,
                                                'can_comment': can_comment,
                                                "val_comment":val_comment
                                                 })


def bookliste(request):
    form = Search()
    # print(request.GET)
    if "search_form" in request.GET:
        # print(request.GET.get('search_form'))
        form_em = Search(request.GET)
        if form_em.is_valid():
            search_text = form_em.cleaned_data['search_form']
            context = {
                'book': Book.objects.filter(Q(name__icontains=search_text) | Q(category__name__icontains=search_text) | Q(author__name__icontains=search_text) ),
                "form": form,
            }
    else:
        context = {
            'book': Book.objects.all(),
            "form": form,
        }
    return render(request, 'bookliste.html', context)


def contest(request):
    context = {'book': Book.objects.all()}
    return render(request, 'contest.html', context)


def category_bookliste(request, category_id):
    context = {'book': Book.objects.filter(category=category_id)}
    return render(request, "bookliste.html", context)


def like(request, book_id):
    customuser = CustomUser.objects.get(user=request.user)
    book = Book.objects.get(id=book_id)
    if Like.objects.filter(user=customuser, book=book).exists():
        if not Like.objects.filter(user=customuser, book=book, vote=True).exists():
            like = Like.objects.get(user=customuser, book=book)
            like.vote = True
            like.save()
    else:
        Like.objects.create(user=customuser, book=book, vote=True)
    return redirect("bookdetail_page", book_id=book_id)


def dislike(request, book_id):
    customuser =CustomUser.objects.get(user=request.user)
    book = Book.objects.get(id=book_id)
    if Like.objects.filter(user=customuser, book=book).exists():
        if not Like.objects.filter(user=customuser, book=book, vote=False).exists():
            like = Like.objects.get(user=customuser, book=book)
            like.vote = False
            like.save()
    else:
        Like.objects.create(user=customuser, book=book, vote=False)
    return redirect("bookdetail_page", book_id=book_id)


def author_list(request, auth_id):
    context = {'book': Book.objects.filter(author=auth_id)}
    return render(request, "bookliste.html", context)


def bookmark(request, book_id):
    book = Book.objects.get(id=book_id)
    if Bookmark.objects.filter(user=request.user).exists():
        if Bookmark.objects.filter(user=request.user, book=book).exists():
            bookmarkbooks = Bookmark.objects.get(user=request.user)
            bookmarkbooks.book.remove(book)
            bookmarkbooks.save()
        else:
            bookmarkbooks = Bookmark.objects.get(user=request.user)
            bookmarkbooks.book.add(book)
            bookmarkbooks.save()
    else:
        bookmark_obj = Bookmark.objects.create(user=request.user)
        bookmark_obj.book.add(book)
        bookmark_obj.save()
    return redirect("bookdetail_page", book_id=book_id)


def login_user(request):
    if request.method=="POST":
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('booklist page')
        else:
            print("i can not")
    # authenticate
    # login
    # session va cookie 
    return render(request, "login.html")

def add_comment(request, book_id):
    if request.method=="POST":
        add_commit = request.POST['add_commit']
        add_title = request.POST['add_title']
        print(request.POST)
        book = Book.objects.get(id=book_id)
        print(request.user)
        customuser = CustomUser.objects.get(user=request.user)  
        print("user = ",customuser, "book = ",book)
        Comment.objects.create(user=customuser , book=book , title=add_title , content=add_commit)    
    return redirect("bookdetail_page", book_id=book_id)

def edit_comment(request, book_id):
    if request.method=="POST":
        print('HEREEE')
        add_commit = request.POST['add_commit']
        add_title = request.POST['add_title']
        book = Book.objects.get(id=book_id)
        customuser = CustomUser.objects.get(user=request.user) 
        my_Comment=Comment.objects.filter(user_id=customuser , book_id=book).update(title=add_commit, content=add_title)
        # print(my_Comment[0])
        # print('======+++++++')
        # print(add_title)
        # my_Comment[0].content = 'NEW'
        # print('+_+_+_++_+_++')
        # print(my_Comment[0].content)
        # my_Comment[0].save()
        # print(" im saved")
        # Comment.objects.update(my_Comment[0])
        # Comment.objects.update(my_Comment[0])   
    return redirect("bookdetail_page", book_id=book_id)

def new_register(request):
    if request.method=="POST":
        add_username=request.POST.get('username')
        add_password=request.POST.get('password')
        add_confirm=request.POST.get('confirm')
        add_email=request.POST.get('useremail')
        if add_password==add_confirm:
            user = User.objects.create_user(username=add_username, password=add_password, email=add_email)
            debt_value=Debt.objects.create(amount=0)
            CustomUser.objects.create(user=user, Debt=debt_value)
            user.save()

            return redirect("login_page")
        else:
            return render(request,"register.html")
    # capcha_list=["iranaian", "davazdah", "chekhabar", "programmers", "python", "ziaei"]
    # for i in capcha_list:
        # data
    # cap = ImageCaptcha(width=90, height=90)
    # data = cap.generate(i)
    # cap.write(i , "c.png")
    return render(request,"register.html")

def logout_user(request):
    logout(request)
    return redirect("login_page")

def profile(request):
    if request.user.is_authenticated :
        customuservalue = CustomUser.objects.get(user=request.user)
        return render (request,"profile.html",customuservalue)    
    else:
        return redirect("login_page")

def addbook(request, ):
    return render(request, 'addbook.html',)
   
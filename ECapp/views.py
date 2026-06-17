from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
from ECapp.models import AccountUser, ShoppingItem, ShoppingItemsincart
from ECapp.forms import RegisterUserForm, LoginForm, RegisterUser1Form


class index(View):
    def get(self, request):
        return redirect(reverse("ECapp:main"))


class login(View):

    def get(self, request):
        if request.session.get('is_login',None):
            return redirect(reverse("ECapp:main"))
        
        form = LoginForm(request.GET)
        context = {
            "form":form,
        }
        return render(request, "login.html", context)
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if not form.is_valid():
            context = {
                "form" : form,
            }
            return render(request, "login.html", context)        
        
        user_check = {
            'user_id':request.POST["user_id"],
            'password':request.POST["password"],
        }
        if AccountUser.objects.filter(**user_check):
            request.session['is_login'] = True
            request.session["user_id"] = request.POST["user_id"]
            queryset = AccountUser.objects.get(user_id=request.session["user_id"])
            context = {
                "flag" : True,
                "name" : queryset.name
            }
            return render(request, "main.html", context)
        else:
            context = {
                "form" : form,
                "flag" : False
            }
            return render(request, "login.html", context)
        


class register_user(View):

    def get(self, request):
        form = RegisterUser1Form(request.GET)
        context = {
            "form":form
        }
        return render(request, "registerUser.html", context)
    
    
    def post(self, request, *args, **kwargs):
        form = RegisterUser1Form(request.POST)
        if not form.is_valid():
            context = {
                "form" : form,
            }
            return render(request, "registerUser.html", context)

        context = {
          "form":form
        }

        return render(request, "registerUserConfirm.html", context) 
    


class register_user_confirm(View):

    def get(self, request):
        form = RegisterUserForm(request.GET)
        context = {
            "form":form
        }
        return render(request, "registerUserConfirm.html", context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        
        context={
            "form":form
        }

        return render(request, "registerUserCommit.html", context) 
    

class register_user_commit(View):

    def get(self, request):
        form = RegisterUserForm(request.GET)
        context = {
            "form":form
        }
        return render(request, "registerUserCommit.html", context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if not form.is_valid():
            context = {
                "form" : form,
            }
            return render(request, "registerUserConfirm.html", context)
        user = AccountUser()
        user.user_id = request.POST["user_id"]
        user.password = request.POST["password"]
        user.name = request.POST["name"]
        user.address = request.POST["address"]
        user.save()

        context={
            "name":user.name
        }

        return render(request, "registerUserCommit.html", context) 
    

class main(View):

    def get(self, request):
        if request.session.get('is_login',None):
            queryset = AccountUser.objects.get(user_id=request.session["user_id"])
            context = {
                "is_login" : request.session.get('is_login'),
                "name" : queryset.name
            }
            return render(request, "main.html",context)
        else:
            return render(request, "main.html")
       

    def post(self, request):
        return render(request, "main.html")
    
class logout(View):

    def get(self, request):
        request.session.flush()
        return redirect(reverse("ECapp:login"))
       

    def post(self, request):
        pass




class user_info(View):

    def get(self, request):
        queryset = AccountUser.objects.get(user_id = request.session.get("user_id"))
        context = {
            "user_id":queryset.user_id,
            "password":queryset.password,
            "name":queryset.name,
            "address":queryset.address
        }
        return render(request, "userInfo.html",context)

    def post(self, request):
        pass

class update_user(View):
    def get(self, request):
        queryset = AccountUser.objects.get(user_id = request.session.get("user_id"))
        context = {
            "user_id":queryset.user_id,
            "name":queryset.name,
            "address":queryset.address
        }
        return render(request, "updateUser.html", context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        for field in form.fields.values():
                field.widget.attrs['readonly'] = True
        if not form.is_valid():
            queryset = AccountUser.objects.get(user_id = request.session.get("user_id"))
            context = {
                "form" : form,
                "user_id":queryset.user_id,
                "name":queryset.name,
                "address":queryset.address,
                "flag":False
            }
            return render(request, "updateUser.html", context)
        
        context = {
                "form" : form,
        }
        return render(request, "updateUserConfirm.html", context)
        


class update_user_confirm(View):
    def get(self, request):
        form = RegisterUserForm(request.GET)
        
        for field in form.fields.values():
                field.widget.attrs['readonly'] = True

        context = {
            "form":form
        }
        return render(request, "updateUserConfirm.html", context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        
        for field in form.fields.values():
                field.widget.attrs['readonly'] = True


        user = AccountUser()
        user.user_id = request.POST["user_id"]
        user.password = request.POST["password"]
        user.name = request.POST["name"]
        user.address = request.POST["address"]
        user.save()

        context={
            "form":form
        }

        return render(request, "updateUserCommit.html", context) 

        


class update_user_commit(View):

    def get(self, request):
        form = RegisterUserForm(request.GET)
        context = {
            "form":form
        }
        return render(request, "updateUserCommit.html", context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        
        
        context={
            "form":form
        }
        return render(request, "updateUserCommit.html",context)
    


class with_draw_confirm(View):

    def get(self, request):
        queryset = AccountUser.objects.get(user_id = request.session.get("user_id"))
        context = {
            "name":queryset.name,
        }
        return render(request, "withdrawConfirm.html",context)

    def post(self, request):
        queryset = AccountUser.objects.get(user_id = request.session.get("user_id"))
        context = {
            "name":queryset.name
        }
        request.session.flush()
        queryset.delete()

        return render(request, "withdrawCommit.html", context)
    


class with_draw_commit(View):

    def get(self, request):
        
        return render(request, "withdrawCommit.html")

    def post(self, request):
        pass



class search_result(View):

    def get(self, request):
        return render(request, "searchResult.html")

    def post(self, request):
        items = ShoppingItem()
    
        
        if request.POST.get("keyword"):
            if request.POST.get("btype") == "すべて":
                items = ShoppingItem.objects.filter(name__icontains=request.POST.get("keyword") )
            elif request.POST.get("btype") == "鞄" :
                condition={"category_id":1, "name__icontains":request.POST.get("keyword")}
                items = ShoppingItem.objects.filter(**condition)
            else:
                condition={"category_id":2, "name__icontains":request.POST.get("keyword")}
                items = ShoppingItem.objects.filter(**condition)
        else:
            if request.POST.get("btype") == "すべて":
                items = ShoppingItem.objects.all()
            elif request.POST.get("btype") == "鞄" :
                items = ShoppingItem.objects.filter(category_id = 1)
            else:
                items = ShoppingItem.objects.filter(category_id = 2)


        context = {
            "keyword":request.POST.get("keyword"),
            "category":request.POST.get("btype"),
            "items":items
        }
        return render(request, "searchResult.html",context)



class item_detail(View):

    def get(self, request, item_id):
        print("POSTデータ:", request.POST)
        print("URLのitem_id:", item_id) 
        item = ShoppingItem.objects.get(item_id = item_id)
        count = range(1,item.stock+1)
        context = {
            "item":item,
            "count":count
        }
        return render(request, "itemDetail.html",context)

    def post(self, request):
        pass


class cart(View):

    def get(self, request):
        if request.session.get("is_login"):
            cartitems = ShoppingItemsincart.objects.filter(
                user_id=request.session.get("user_id")
            ).select_related("item")
            total = sum(item.item.price * item.amount for item in cartitems)
            context = {
                "cartitems": cartitems,
                "sum": total
            }
            return render(request, "cart.html", context)
        else:
            return redirect(reverse("ECapp:login"))

       

    def post(self, request):
        if request.session.get("is_login"):

            if ShoppingItemsincart.objects.filter(
                user_id=request.session.get("user_id"),
                item_id=request.POST.get("item_id")
            ).exists():

                itemscart = ShoppingItemsincart.objects.get(
                    user_id=request.session.get("user_id"),
                    item_id=request.POST.get("item_id")
                )

                itemscart.amount += int(request.POST["btype"])

            else:
                itemscart = ShoppingItemsincart()
                itemscart.user_id = request.session.get("user_id")
                itemscart.item_id = request.POST.get("item_id")
                itemscart.amount = int(request.POST["btype"])

            itemscart.save()
            return redirect("ECapp:cart")

        else:
            return redirect(reverse("ECapp:login"))
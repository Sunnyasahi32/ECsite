from django.db import models

class AccountUser(models.Model):

    class Meta:
        db_table = "account_user"

    user_id = models.CharField(verbose_name="会員ID", max_length=128, primary_key=True)
    password = models.CharField(verbose_name="パスワード", max_length=256)
    name = models.CharField(verbose_name="名前", max_length=128)
    address = models.CharField(verbose_name="住所", max_length=256)


    # 管理サイトに表示する文字列を指定
    def __str__(self):
        return self.name
    
class ShoppingCategory(models.Model):

    class Meta:
        db_table = "Shopping_category"

    category_id = models.IntegerField(verbose_name="カテゴリID", primary_key=True)
    name = models.CharField(verbose_name="名前", max_length=256)


    # 管理サイトに表示する文字列を指定
    def __str__(self):
        return self.name
    
class ShoppingItem(models.Model):

    class Meta:
        db_table = "Shopping_item"

    item_id = models.IntegerField(verbose_name="商品ID", primary_key=True)
    name = models.CharField(verbose_name="商品名", max_length=128)
    manufacturer = models.CharField(verbose_name="メーカーの色", max_length=32)
    color = models.CharField(verbose_name="商品の色", max_length=16)
    price = models.IntegerField(verbose_name="価格")
    stock = models.IntegerField(verbose_name="在庫数")
    recommended = models.BooleanField(verbose_name="オススメ", default=False)
    category = models.ForeignKey(ShoppingCategory,verbose_name="カテゴリID", on_delete=models.CASCADE)

    # 管理サイトに表示する文字列を指定
    def __str__(self):
        return self.name
    
class ShoppingItemsincart(models.Model):

    class Meta:
        db_table = "Shopping_itemsincart"

    amount = models.IntegerField(verbose_name="数量")
    booked_date = models.DateTimeField(verbose_name="登録日", auto_now_add=True)
    item = models.ForeignKey(ShoppingItem, verbose_name="商品ID", on_delete=models.CASCADE)
    user = models.ForeignKey(AccountUser, verbose_name="会員ID", on_delete=models.CASCADE)



    # 管理サイトに表示する文字列を指定
    def __str__(self):
        return self.name
    
class ShoppingPurchase(models.Model):

    class Meta:
        db_table = "Shopping_purchase"

    purchase_id = models.IntegerField(verbose_name="注文ID", primary_key=True)
    destination = models.CharField(verbose_name="配送先", max_length=256)
    booked_date = models.DateTimeField(verbose_name="注文日", auto_now_add=True)
    cancel = models.BooleanField(verbose_name="オススメ", default=False)
    user = models.ForeignKey(AccountUser, verbose_name="注文者", on_delete=models.CASCADE)



    # 管理サイトに表示する文字列を指定
    def __str__(self):
        return self.name
    
class ShoppingPurchaseDetail(models.Model):

    class Meta:
        db_table = "Shopping_purchasedetail"

    purchase_detail_id = models.IntegerField(verbose_name="注文詳細ID", primary_key=True)
    amount = models.IntegerField(verbose_name="注文数")
    item = models.ForeignKey(ShoppingItem, verbose_name="商品ID", on_delete=models.CASCADE)
    purchase = models.ForeignKey(ShoppingPurchase, verbose_name="注文ID", on_delete=models.CASCADE)



    # 管理サイトに表示する文字列を指定
    def __str__(self):
        return self.name
    
class AdministratorAdmin(models.Model):

    class Meta:
        db_table = "administrator_admin"

    admin_id = models.CharField(verbose_name="注文詳細ID", max_length=128, primary_key=True)
    password = models.CharField(verbose_name="パスワード", max_length=256)




    # 管理サイトに表示する文字列を指定
    def __str__(self):
        return self.name
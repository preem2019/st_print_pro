from django.db import models


class Banner(models.Model):
    title = models.CharField("หัวข้อแบนเนอร์", max_length=200, blank=True)
    image = models.ImageField("รูปภาพแบนเนอร์", upload_to="banners/")
    link = models.URLField("ลิงก์ (ถ้ามี)", blank=True)

    def __str__(self):
        return self.title or f"Banner {self.id}"


class Product(models.Model):
    name = models.CharField("ชื่อสินค้า", max_length=255)
    image = models.ImageField("รูปสินค้า", upload_to="products/")
    description = models.TextField("รายละเอียด", blank=True)

    def __str__(self):
        return self.name

from django.db import models


class Pizza(models.Model):
    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]

    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default="M")  

    def __str__(self) -> str:
        return f"{self.name} ({self.get_size_display()})"  


class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def total_price(self) -> int:
        return self.count * self.pizza.price
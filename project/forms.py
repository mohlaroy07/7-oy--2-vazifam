from django import forms
from .models import Pizza, Order


class PizzaForm(forms.Form):
    image = forms.ImageField(label="Pizza rasmi", required=True)
    name = forms.CharField(max_length=128, label="Pizza nomi")
    price = forms.IntegerField(label="Narxi")
    size = forms.ChoiceField(choices=Pizza.SIZE_CHOICES, label="Pizza o'lchami", required=True)  # O'lcham tanlash qo'shildi

    def __init__(self, *args, **kwargs) -> None:
        instance = kwargs.pop("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields["image"].required = False

        for field_name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def create(self):
        return Pizza.objects.create(**self.cleaned_data)


class OrderForm(forms.Form):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), label="Pizza")  # "Mahsulot" o'rniga "Pizza"
    count = forms.IntegerField(label="Soni")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def clean_count(self):
        count = self.cleaned_data.get("count", -1)

        if count <= 0:
            raise ValueError("Pizza soni 0 dan katta bo'lishi kerak")

        return count

    def create(self):
        return Order.objects.create(**self.cleaned_data)

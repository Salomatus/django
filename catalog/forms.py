from django.forms import ModelForm

from catalog.models import Product

from django.core.exceptions import ValidationError


FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "дёшево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "owner")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["foto"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control"})

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name.lower() in FORBIDDEN_WORDS:
            raise ValidationError("Название содержит запрещенное слово")
        return name

    def clean(self):
        if self.cleaned_data.get("price") < 0:
            raise ValidationError("Цена не может быть отрицательной")
        else:
            return self.cleaned_date

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")

        return price

from django import forms
from tracker.models import Transaction, Category

class TransactionForm(forms.ModelForm):
    TYPE_CHOICES = [
        ('income', 'Доход'),
        ('expense', 'Расход'),
    ]

    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        label="Тип транзакции"
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect(),
        label="Категория"
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Введите описание'
        }),
        label="Описание"
    )

    amount = forms.DecimalField(
        min_value=0,
        label="Сумма"
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Дата"
    )

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is None:
            raise forms.ValidationError("Это поле не может быть пустым.")
        if amount <= 0:
            raise forms.ValidationError("Сумма должна быть положительным числом.")
        return amount 

    class Meta:
        model = Transaction
        fields = ['category', 'type', 'description', 'amount', 'date']

import django_filters
from django import forms
from tracker.models import Transaction, Category

class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.ChoiceFilter(
        choices = Transaction.TRANSACTION_TYPE_CHOISES,
        field_name='type',
        lookup_expr='iexact',
        label='Тип Транзакции',  
        empty_label='Все Типы',
    )
    start_date = django_filters.DateFilter(
    field_name='date', 
    lookup_expr='gte', 
    label='Начальная Дата',
    widget=forms.DateInput(attrs={'type': 'date'}),
    )
    end_date = django_filters.DateFilter(
    field_name='date', 
    lookup_expr='lte', 
    label='Конечная Дата',
    widget=forms.DateInput(attrs={'type': 'date'}),
    )
    category = django_filters.ModelMultipleChoiceFilter(
    queryset=Category.objects.all(), 
    widget=forms.CheckboxSelectMultiple(), 
    )
    class Meta:
        model = Transaction
        fields = ('transaction_type', 'start_date', 'end_date', 'category')
from import_export import resources, fields
from tracker.models import Transaction, Category
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import Widget

class TypeWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        if value == 'Доход':
            return 'income'
        elif value == 'Расход':
            return 'expense'
        return value

    def render(self, value, obj=None):
        if value == 'income':
            return 'Доход'
        elif value == 'expense':
            return 'Расход'
        return value 
class TransactionResource(resources.ModelResource):
    amount = fields.Field(column_name='Сумма', attribute='amount')
    type = fields.Field(column_name='Тип', attribute='type', widget=TypeWidget())
    description = fields.Field(column_name='Описание', attribute='description')
    date = fields.Field(column_name='Дата', attribute='date')
    category = fields.Field(column_name='Категория', attribute='category', widget=ForeignKeyWidget(Category, field='name'))

    def after_init_instance(self, instance, new, row, **kwargs):
        instance.user = kwargs.get('user')

    class Meta:
        model = Transaction
        fields = ('amount', 'type', 'description', 'date', 'category')
        import_id_fields = ('amount', 'type', 'description', 'date', 'category')
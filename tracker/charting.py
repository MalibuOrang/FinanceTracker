import plotly.express as px
from django.db.models import Sum
from tracker.models import Category
def plot_income_expeses_bar_chart(qs):
    x_vals = ['Доход', 'Расход']
    total_income = qs.filter(type='income').aggregate(
        total=Sum('amount')
    )['total']
    total_expenses = qs.filter(type='expense').aggregate(
        total=Sum('amount')
    )['total']
    fig = px.bar(x=x_vals, y=[total_income, total_expenses])
    fig.update_traces(marker_color="#10B981")  
    fig.update_layout(
    plot_bgcolor="#111827",
    paper_bgcolor="#111827",
    font_color="white"
    )
    return fig

def plot_category_pie_chart(qs):
    count_per_category = qs.order_by('category').values('category').annotate(total=Sum('amount'))
    category_pks = count_per_category.values_list('category', flat=True).order_by('category')
    categories = Category.objects.filter(pk__in=category_pks).order_by('pk').values_list('name', flat=True)
    total_amounts = count_per_category.order_by('category').values_list('total', flat = True)
    fig = px.pie(values=total_amounts, names=categories)
    fig.update_layout(title_text='Суммарные по категориям')
    fig.update_traces(
    marker=dict(
        colors=["#10B981", "#34D399", "#059669", "#6EE7B7"]
    ),
    textfont_color="white"
    )
    fig.update_layout(
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white"
    )
    return fig
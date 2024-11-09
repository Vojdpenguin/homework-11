from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Quote, Author
from .forms import AuthorForm, QuoteForm

def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_detail(request, id):
    author = get_object_or_404(Author, pk=id)

    return render(request, 'quotes/author.html', {'author': author})

@login_required
def create_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()

            return redirect('quotes:root')
        else:
            return render(request, 'quotes/create_author.html', {'author_form': author_form})
    return render(request, 'quotes/create_author.html', {'author_form': AuthorForm()})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:root')
        else:
            return render(request, 'quotes/add_quote.html', {'form': form})

    return render(request, 'quotes/add_quote.html', {'form': QuoteForm()})




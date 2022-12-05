from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Stories, Stories_i18n, Pages, Languages, Categories, Categories_i18n
from .forms import StoriesForm, Stories_i18nForm, PagesForm
from django.views.generic import DetailView, UpdateView, DeleteView, View, ListView


class LanguageCategory:
    def get_languages(self):
        return Languages.objects.all()

    def get_categories(self):
        return Categories_i18n.objects.filter(language=1)

    hidden123 = False


############################################## View #############################################################

class StoriesView(LanguageCategory, ListView):
    model = Stories
    template_name = 'main_app/stories.html'
    context_object_name = 'stories_key'


class AboutView(View):
    def get(self, request):
        return render(request, 'main_app/about.html')


class StoryDetailView(DetailView):
    context_object_name = 'key_story'
    model = Stories
    queryset = Stories.objects.prefetch_related('storiesi18n_stories').all()
    template_name = 'main_app/story_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories_i18n'] = self.object.storiesi18n_stories.all()
        return context


class Story_i18nDetailView(DetailView):
    context_object_name = 'page_story'
    model = Stories_i18n
    queryset = Stories_i18n.objects.prefetch_related('pages_storiesi18n').all()
    template_name = 'main_app/story_i18n_details.html'

    def get_context_data(self, **kwargs):
        # context = super(Story_i18nDetailView, self).get_context_data(**kwargs)
        # stories_i18n = Stories_i18n.objects.get(id=self.kwargs.get('pk_st', ''))
        # context['page_story'] = stories_i18n
        context = super().get_context_data(**kwargs)
        context['pages'] = self.object.pages_storiesi18n.all()
        return context


class LanguagesView(ListView):
    model = Languages
    template_name = 'main_app/language.html'
    context_object_name = 'language'


class CategoriesView(ListView):
    model = Categories
    template_name = 'main_app/category.html'
    context_object_name = 'category'

    def my_func(self):
        return 'Hello from model'


class CategoryDetailView(DetailView):
    context_object_name = 'key_category'
    model = Categories
    queryset = Categories.objects.prefetch_related('categoriesi18n_categories').all()
    template_name = 'main_app/category_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_i18n'] = self.object.categoriesi18n_categories.all()
        return context


class FilterStoriesView(LanguageCategory, ListView):
    template_name = 'main_app/stories.html'
    context_object_name = 'stories_key'

    def get_queryset(self):
        print("test1", self.request.GET.get("hidden_val"))
        print("test2", Stories.objects.filter(hide_in_stories=self.request.GET.get("hidden_val")))

        queryset = Stories.objects.filter(
            category__in=self.request.GET.getlist("categ_val")
        )
        # list_categories = self.request.GET.getlist("categ_val")
        # list_hidden = self.request.GET.getlist("hidden_val")
        #
        # if  list_categories and list_hidden:
        #     queryset = Stories.objects.filter(
        #         category__in=list_categories,
        #         hide_in_stories=self.request.GET.get("hidden_val")
        #     )
        # else:
        #     queryset = Stories.objects.filter(
        #         Q(category__in=list_categories) |
        #         Q(hide_in_stories=list_hidden)
        #     )
        return queryset


############################################## Add #############################################################

def add_story(request):
    error = ''
    if request.method == 'POST':
        form_story = StoriesForm(request.POST)  # getting all data which was filled

        if form_story.is_valid():  # validation
            story = form_story.save()
            # redirection on successful save
            return redirect('/story=' + str(story.pk) + '/')
    else:
        error = 'Filling error'
        form_story = StoriesForm()  # if validation is fail we keep data in forms

    data = {
        'form_story': form_story,
        'error_add': error
    }
    return render(request, 'main_app/add_story.html', data)


def add_category(request):
    error = ''
    return render(request, 'main_app/add_story.html')


def add_story_i18n(request, pk_st):
    error = ''
    if request.method == 'POST':
        form_story_i18n = Stories_i18nForm(request.POST)
        if form_story_i18n.is_valid():
            story_i18n = form_story_i18n.save()
            return redirect(f'/story={story_i18n.story}/story_i18n={story_i18n.pk}/')

    else:
        error = 'Filling error'
        form_story_i18n = Stories_i18nForm(initial={'story': pk_st})

    data = {
        'form_story_i18n': form_story_i18n,
        'error_add': error
    }
    return render(request, 'main_app/add_story_i18n.html', data)


def add_page(request, pk_st, pk_i18n):
    error = ''
    if request.method == 'POST':
        form_page = PagesForm(request.POST)
        if form_page.is_valid():
            page = form_page.save()
            return redirect(f'/story={page.story_i18n.story}/story_i18n={page.story_i18n.pk}/')
    else:
        error = 'Filling error'
        form_page = PagesForm(initial={'story_i18n': pk_i18n})

    data = {
        'form_page': form_page,
        'error_add': error
    }
    return render(request, 'main_app/add_page.html', data)


############################################## Edit #############################################################

class StoryEditView(UpdateView):
    template_name = 'main_app/edit_story.html'
    model = Stories
    form_class = StoriesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = get_object_or_404(Stories, pk=self.kwargs['pk'])
        context['form_story'] = StoriesForm(instance=story)
        return context


class Story_i18nEditView(UpdateView):
    template_name = 'main_app/edit_story_i18n.html'
    model = Stories_i18n
    form_class = Stories_i18nForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uu = self.kwargs['pk']
        story_i18n = get_object_or_404(Stories_i18n, pk=self.kwargs['pk'])
        context['form_story_i18n'] = Stories_i18nForm(instance=story_i18n)
        return context


class PageEditView(UpdateView):
    template_name = 'main_app/edit_page.html'
    model = Pages
    form_class = PagesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = get_object_or_404(Pages, pk=self.kwargs['pk'])
        context['form_page'] = PagesForm(instance=page)
        return context


##############################################  #############################################################


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main_app/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

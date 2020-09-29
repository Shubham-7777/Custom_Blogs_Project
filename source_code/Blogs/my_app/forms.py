from django import forms
from .models import BlogPost

"""
class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)
"""


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        """print(dir(self))
        print(instance)
        print(instance.title)
        print(instance.slug)
        print(instance.content)"""
        title = self.cleaned_data.get('title')
        slug = self.cleaned_data.get('slug')
        qs_title = BlogPost.objects.filter(title__iexact=title)  # or__icontains
        # qs_slug = BlogPost.objects.filter(slug__iexact=slug)  # or__icontains
        if instance is not None:
            qs_title = qs_title.exclude(pk=instance.pk)
        if qs_title.exists():
            raise forms.ValidationError("This title is already been used ")
        return title
        """elif qs_slug.exists():
            raise forms.ValidationError("This slug is already been used ")
        return title"""

from django.contrib import admin
from .models import tutorial
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class tutorialAdmin(admin.ModelAdmin):
	fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_Datetime"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()},
	}

admin.site.register(tutorial,tutorialAdmin)
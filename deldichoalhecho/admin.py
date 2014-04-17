from django.contrib import admin
from .models import Promise, Fulfillment, InformationSource, Category, VerificationDocument
from popolo.models import Person
from django.forms import ModelForm

# Register your models here.

class FulfillmentInlineAdmin(admin.StackedInline):
	model = Fulfillment

class InformationSourceInline(admin.TabularInline):
    model = InformationSource


class VerificationDocumentInline(admin.TabularInline):
    model = VerificationDocument

class PromiseAdmin(admin.ModelAdmin):
    inlines = (FulfillmentInlineAdmin, InformationSourceInline, VerificationDocumentInline, )

admin.site.register(Promise, PromiseAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Person, PersonAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

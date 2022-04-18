
from django.contrib import admin
from django.db.models import Q

from khodro45_app.models import Appointment, Auction, Bid, Brand, Inspection 


# admin.site.register(Inspection)
# admin.site.register(Auction)
# admin.site.register(Bid)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id","title","created_time","modified_time")
    list_filter = ("title","created_time","modified_time")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id","brand","customer","modified_time")
    list_filter = ("brand","modified_time")


@admin.register(Inspection)
class InspetionAdmin(admin.ModelAdmin):
    list_display = ("id","status","appointmet","modified_time")
    list_filter = ("status","modified_time")
    search_fields = ("appointmet","modified_time")


class BidFilter(admin.SimpleListFilter):
    title = 'bider ID'
    parameter_name = 'bider_username'
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        return ((None, None),)

    def choices(self, changelist):
        query_params = changelist.get_filters_params()
        query_params.pop(self.parameter_name, None)
        all_choice = next(super().choices(changelist))
        all_choice['query_params'] = query_params
        yield all_choice

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(bider=value)

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):

    list_display = ("id","start_price","bider","bider_id","inspection","modified_time")
    list_filter = ("start_price","modified_time",BidFilter)



@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    
    list_display = ("id","bider","modified_time")
    list_filter = ("bider","modified_time")

# class BidAdAdminFilter(AdminAdvancedFiltersMixin, admin.ModelAdmin):
#     list_display = ("id","bider","modified_time")
#     advanced_filter_fields = ("bider","modified_time")


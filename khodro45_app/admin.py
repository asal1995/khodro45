
from django.contrib import admin

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


class BidFilter(admin.SimpleListFilter):
    title= 'bider'
    parameter_name = "winner"



    def lookups(self, request, model_admin):
        
            return ((),)
          
        


    def queryset(self, request, queryset):
       
        if self.value():
           
            return queryset.distinct().filter(winner__isnull=False)
        if self.value():
           
            return queryset.distinct().filter(winner__isnull=True)

   



@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):

    list_display = ("id","start_price","bider","inspection","modified_time")
    list_filter = (BidFilter ,)
   


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    
    list_display = ("id","bider","modified_time")
    list_filter = ("bider","modified_time")

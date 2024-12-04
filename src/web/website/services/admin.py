from django.contrib import admin
from .models import ServiceCategory, Service, ServiceReview, ServiceFeature, ServicePricing, ServiceInquiry


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')


@admin.register(ServiceReview)
class ServiceReviewAdmin(admin.ModelAdmin):
    list_display = ('service', 'reviewer_name', 'rating', 'created_at')
    list_filter = ('service', 'rating')
    search_fields = ('reviewer_name', 'comment')


@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('service', 'feature_name')
    list_filter = ('service',)
    search_fields = ('feature_name',)


@admin.register(ServicePricing)
class ServicePricingAdmin(admin.ModelAdmin):
    list_display = ('service', 'package_name', 'price')
    list_filter = ('service',)
    search_fields = ('package_name',)


@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):
    list_display = ('service', 'user_name', 'email', 'created_at')
    list_filter = ('service',)
    search_fields = ('user_name', 'email', 'message')

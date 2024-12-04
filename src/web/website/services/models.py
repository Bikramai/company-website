from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)  # Category name (e.g., Development, Branding)
    description = models.TextField(blank=True, null=True)  # Optional description of the category

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE,
                                 related_name='services')  # Links each service to a category
    name = models.CharField(max_length=150)  # Name of the service (e.g., Designing, Consulting)
    description = models.TextField()
    # A detailed description of the service
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    image1 = models.ImageField(upload_to='services/', blank=True, null=True) # Optional image for the service
    is_active = models.BooleanField(default=True)  # Whether the service is active or not

    def __str__(self):
        return self.name


class ServiceReview(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')  # Link to the service
    reviewer_name = models.CharField(max_length=100)  # Name of the reviewer
    rating = models.PositiveIntegerField(default=1)  # Rating out of 5
    comment = models.TextField(blank=True, null=True)  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the review

    def __str__(self):
        return f'Review for {self.service.name} by {self.reviewer_name}'


class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')  # Link to the service
    feature_name = models.CharField(max_length=100)  # Name of the feature
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.feature_name


class ServicePricing(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='pricing')  # Link to the service
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the service
    package_name = models.CharField(max_length=100)  # Name of the pricing package
    description = models.TextField(blank=True, null=True)  # Optional description of what is included

    def __str__(self):
        return f'{self.package_name} for {self.service.name}'


class ServiceInquiry(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='inquiries')  # Link to the service
    user_name = models.CharField(max_length=100)  # Name of the person making the inquiry
    email = models.EmailField()  # Email of the inquirer
    message = models.TextField()  # Inquiry message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the inquiry

    def __str__(self):
        return f'Inquiry by {self.user_name} for {self.service.name}'

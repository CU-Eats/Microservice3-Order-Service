from django.db import models

class Order(models.Model):
    order_id = models.IntegerField(null=False)
    product_name = models.CharField(max_length=256, null=False)
    user_name = models.CharField(max_length=256, null=False)
    user_id = models.IntegerField(null=False)
    restaurant_name = models.CharField(max_length=256, null=False)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = (
            ('user_name', 'product_name'),
            ('restaurant_name', 'created_at'),
        )


    def __str__(self):
        return '{} ordered {} from at {}'.format(
            self.user_id,
            self.product_name,
            self.restaurant_name,
            self.created_at
        )
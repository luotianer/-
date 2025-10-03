from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类名称")
    order = models.IntegerField(default=0, verbose_name="排序")

    class Meta:
        verbose_name = "菜品分类"
        verbose_name_plural = "菜品分类"
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="菜品名称")
    description = models.TextField(blank=True, verbose_name="描述")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="价格")
    image = models.ImageField(
        upload_to='dishes/',
        blank=True,
        null=True,
        verbose_name="菜品图片"
    )
    is_available = models.BooleanField(default=True, verbose_name="是否可售")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='dishes',
        verbose_name="分类"
    )

    class Meta:
        verbose_name = "菜品"
        verbose_name_plural = "菜品"

    def __str__(self):
        return self.name
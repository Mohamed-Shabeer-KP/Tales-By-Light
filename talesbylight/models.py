from django.db import models

class voteData (models.Model):
    class Meta:
        verbose_name = ("vote_data")
        verbose_name_plural = ("vote_datas")

    def __str__(self):
        return self.v_name

    v_name = models.CharField("name", max_length=50)
    v_img_no = models.IntegerField("image_number")
    v_date = models.DateTimeField("Voted at")
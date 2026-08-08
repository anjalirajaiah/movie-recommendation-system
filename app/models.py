from django.db import models

# Movie Table
class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Review Table
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_text = models.TextField()
    sentiment_score = models.FloatField()

    def __str__(self):
        return self.review_text

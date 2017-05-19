from django.db import models


class Album(models.Model):
    #collim name
    artist = models.CharField(max_length=250)
    # Type of data
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return "{} - {}".format(self.album_title, self.artist)


class Song(models.Model):
    # Associate song with album
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)



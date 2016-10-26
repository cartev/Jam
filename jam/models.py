#
# jam/models.py
#

from __future__ import unicode_literals

from django.db import models

# Database Modeling

class Artists(models.Model):
    ArtistName = models.CharField(max_length=255)
    SpotifyID = models.CharField(primary_key=True, max_length=255)
    PrimaryGenre = models.CharField(max_length=255)
    SecondaryGenre = models.CharField(max_length=255)
    
    def __unicode__(self): return u'%s' % (self.ArtistName)
    def toString(self):
        return '%s' % (self.ArtistName)
    def artistID(self):
        return '%s' % (self.SpotifyID)

    #class Meta:
    #     ordering = ['name']
    
class Album(models.Model):
    AlbumTitle = models.CharField(max_length=255)
    SpotifyAlbumID = models.CharField(primary_key=True, max_length=255)
    ArtistID = models.ForeignKey(Artists, on_delete=models.CASCADE)
    Featured = models.BooleanField(default=False)

    def __unicode__(self): return u'%s' % (self.AlbumTitle)
    def toString(self):
        return '%s' % (self.AlbumTitle)
    def isFeatured(self):
        return self.Featured


class Profile(models.Model):
    RealName = models.CharField(max_length=255)
    Username = models.CharField(primary_key=True, max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    # Avatar = models.ImageField()

# This should be inherited from Album
class Review(models.Model):
    AlbumID = models.ForeignKey(Album, on_delete=models.CASCADE)
    Review = models.TextField(default=" ")

    def __unicode__(self): return u'%s' % (self.AlbumTitle)
    def toString(self):
        return '%s' % (self.Review)



from rest_framework import serializers

########################
#  FEATURE WRAPPER CLASS
########################

class Feature(object):

    def __init__(self, name, title, review):
        self.artistName = name
        self.albumTitle = title
        self.featureReview = review

    def __unicode__(self):
        return self.artistName + " " + self.albumTitle + " " + self.featureReview

    def toString(self):
        return self.artistName + " " + self.albumTitle + " " + self.featureReview

    def as_json(self):
        return dict(
            artistName = self.artistName,
            albumTitle = self.albumTitle,
            featureReview = self.featureReview
            )
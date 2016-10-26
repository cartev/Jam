from rest_framework import serializers, viewsets
from jam.models import Artists, Album, Profile, Review
from jam.feature_wrapper import Feature

###################
# API CONFIGURATION
###################

# Serializers define the API representation.
class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artists
        fields = ('ArtistName', 'SpotifyID', 'PrimaryGenre', 'SecondaryGenre')

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('AlbumTitle', 'SpotifyAlbumID', 'AritstID', 'Favorite')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('RealName', 'Username', 'Email')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('AlbumID','Review')


# ViewSets define the view behavior.
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer

def getFeatures():
    featured_albums_list = list(Album.objects.filter(Featured=True))
    features = []
    for x in featured_albums_list:
        review = Review.objects.filter(AlbumID=x.SpotifyAlbumID)[0]
        features.append(Feature(x.ArtistID.ArtistName, x.AlbumTitle, review.Review))
    return features


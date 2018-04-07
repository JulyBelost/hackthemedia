import urllib2


# Download .xml file
#'{0} and {1}'.format('spam', 'eggs')
response = urllib2.urlopen('http://rutube.ru/api/metainfo/tv/{show_id}/video/?season={season_id}&episode={episode_id}'.format(
    show_id = 10,
    season_id = 4,
    episode_id = 3
    ))
xml = response.read()
print (xml)

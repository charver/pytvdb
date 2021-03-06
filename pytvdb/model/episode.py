from lxml import etree
from .exceptions import TVDBException
from . import TVDBType,convert_to_map, convert_to_pythonic_form

class Episode(TVDBType):
    def __init__(self,**kwargs):
        for item in kwargs.keys():
            if item in ['IMDB_ID'] or item.startswith('DVD_'):
                setattr(self,item.lower().replace(' ','_'),kwargs[item])
            else:
                setattr(self,convert_to_pythonic_form(item),kwargs[item])

        self._convert_field(['id','seasonid','combined_episode_number','absolute_number','combined_season','season_number','dvd_season','episode_number','seried_id','ep_img_flag','dvd_discid'],int)
        self._convert_field(['guest_stars'],list)
        self._art_enriched = False


    def __str__(self):
        return "Episode:{%s}" % (str(self.__dict__))

    def enrich_art(self):
        if not self._art_enriched:
            if hasattr(self,'filename') and self.filename is not None:
                self.filename = self._get_art(self.filename)
            self._art_enriched = True

    @staticmethod
    def from_xml(xml):
        args = convert_to_map(xml,'Episode')
        return Episode(**args)
 

from guillotina import interfaces
from guillotina import configure
from guillotina import content
from guillotina import schema

##Content Class FolderAnime StartHere
class IFolderAnime(interfaces.IFolder):
    pass

@configure.contenttype(
    type_name="FolderAnime",
    schema=IFolderAnime,
    #allowed_types = ["Anime"],
    globally_addable = True,
)
class FolderAnime(content.Folder):
    pass
##Content Class FolderAnime StopHere

##Content Class Layout_User StartHere
class IAnime(IFolderAnime):
    id_mal = schema.Int()
    title = schema.TextLine()
    alternative_titles = schema.TextLine()
    start_date = schema.Date()
    end_date = schema.Date()
    synopsis = schema.Text()
    genres = schema.List()
    num_episodes = schema.Int()
    year = schema.Int()
    season = schema.TextLine()
    source = schema.TextLine()
    rating = schema.TextLine()
    local_location = schema.TextLine()

@configure.contenttype(
    type_name="Anime",
    schema=IAnime,
    #behaviors=["guillotina.behaviors.dublincore.IDublinCore"],
    globally_addable = True
)
class Anime(FolderAnime):
    pass
##Content Class Layout_User StopHere
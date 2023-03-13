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
    id = schema.Int()
    anime_name = schema.TextLine()
    description = schema.TextLine()

@configure.contenttype(
    type_name="Anime",
    schema=IAnime,
    #behaviors=["guillotina.behaviors.dublincore.IDublinCore"],
    globally_addable = True
)
class Anime(content.Item):
    pass
##Content Class Layout_User StopHere
#from guillotina import interfaces
from guillotina import configure
#from guillotina import content
#from guillotina import schema
from guillotina import service
from guillotina.interfaces import IResource
from guillotina.interfaces import IResourceSerializeToJson
#from guillotina.interfaces.events import ObjectCreatedEvent
#from guillotina.interfaces import IItemSerialization
from guillotina.interfaces.events import IObjectAddedEvent
from guillotina.transactions import get_tm
from guillotina.utils import find_container, navigate_to
from guillotina.content import create_content
from guillotina.component import get_multi_adapter
from guillotina.component import get_utility
from animedb.content.folder_s import Anime
from requests_oauth2client import BearerAuth
from requests import get
import logging

logger = logging.getLogger("guillotina")

##Service Template StartHere
@configure.service(
    context=IResource,
    method="POST",
    permission="guillotina.AddContent",
    name="@pull_mal",
)
async def pull_mal(context, request):
    param_in = request.query.copy()
    url = "https://api.myanimelist.net/v2/anime/"
    anime_id = param_in['anime_id']
    param = "?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics"
    token = param_in['token']
    hsl = get(url+anime_id+param, auth=BearerAuth(token))
    hsl = hsl.json()

    content_type = "Anime"
    """
    #try:
    if param_in["local"]:
        if param_in["local"] == "laptop":  
            logger.debug(f'hsl: {hsl["title"]}')
            path = "/anime_laptop/"
            container = find_container()
            my_content = await navigate_to(container, path)
            #my_content = folder.async_add(Anime())
            my_content.title = hsl["title"]
            my_content.id = hsl["id"],
            my_content.id_mal = hsl["id"]
            my_content.start_date = hsl["start_date"]
            my_content.end_date = hsl["end_date"]
            my_content.synopsis = hsl["synopsis"]
            my_content.num_episodes = hsl["num_episodes"]
            my_content.source = hsl["source"]
            my_content.local_location = "laptop"
            #await my_content.notify(ObjectCreatedEvent(my_content))
            tm = get_tm()
            await tm.commit()
            #serializer = get_utility(IResourceSerializeToJson, name='serializer')
            #serialized_data = await serializer(my_content, request, IResourceSerializeToJson)
            #return serialized_data
            #content_data = {
                #    "id" : hsl["id"],
                #    "id_mal" : hsl["id"],
                #    "title" : hsl["title"],
                    #alternative_titles : schema.TextLine()
                #    "start_date" : hsl["start_date"],
                #    "end_date" : hsl["end_date"],
                #    "synopsis" : hsl["synopsis"],
                    #"genres" : schema.List(),
                #    "num_episodes" : hsl["num_episodes"],
                    #"year" : hsl["start_date"],
                    #"season" : hsl["start_date"],
                #    "source" : hsl["source"],
                    #"rating" : hsl["start_date"],
                #    "local_location" : "laptop"
            #}
            #navigate_to_container = await navigate_to(container,path)
            #content = await create_content(content_type, **content_data)
            #await navigate_to_container.async_set(content.id, content)
            #logger.debug(f'content: {content} type: {type(content)}')
            #logger.debug(f'content_data: {content_data} type: {type(content_data)}')
            #logger.debug(f'navigate_to_dasboard: {navigate_to_container} type: {type(navigate_to_container)}')
    #except Exception as Argument:
        #logger.debug(f'if param_in["local"]: Argument: {Argument}')"""
    logger.debug(f'test service context: {context}')
    logger.debug(f'test service request: {request}')
    return {"mal": hsl}
##Service Template StopHere
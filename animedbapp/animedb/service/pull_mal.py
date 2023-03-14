from guillotina import interfaces
from guillotina import configure
from guillotina import content
from guillotina import schema
from guillotina.interfaces import IResource
from requests_oauth2client import BearerAuth
from requests import get
import logging

logger = logging.getLogger("guillotina")

##Service Template StartHere
@configure.service(
    context=IResource,
    method="GET",
    permission="guillotina.AccessContent",
    name="@pull_mal",
)
async def pull_mal(context, request):
    param_in = request.query.copy()
    url = "https://api.myanimelist.net/v2/anime/"
    anime_id = param_in['anime_id']
    param = "?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics"
    token = param_in['token']
    hsl = get(url+anime_id+param, auth=BearerAuth(token))
    logger.debug(f'test service context: {context}')
    logger.debug(f'test service request: {request}')
    return {"mal": hsl.json()}
##Service Template StopHere
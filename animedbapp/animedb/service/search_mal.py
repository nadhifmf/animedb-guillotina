#from guillotina import interfaces
from guillotina import configure
#from guillotina import content
#from guillotina import schema
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
    name="@search_mal",
)
async def search_mal(context, request):
    param_in = request.query.copy()
    url = "https://api.myanimelist.net/v2/anime?q="
    q = param_in['anime_kw']
    param = "&limit=500"
    token = param_in['token']
    hsl = get(url+q+param, auth=BearerAuth(token))
    logger.debug(f'test service context: {context}')
    logger.debug(f'test service request: {request}')
    return {"mal": hsl.json()}
##Service Template StopHere
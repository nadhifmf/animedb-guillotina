from guillotina import interfaces
from guillotina import configure
from guillotina import content
from guillotina import schema
from guillotina.interfaces import IResource
import logging

logger = logging.getLogger("guillotina")

##Service Template StartHere
@configure.service(
    context=IResource,
    method="GET",
    permission="guillotina.AccessContent",
    name="@template",
)
async def template_service(context, request):
    logger.debug(f'test service context: {context}')
    logger.debug(f'test service request: {request}')
    return {"dashboard": "test_service"}
##Service Template StopHere
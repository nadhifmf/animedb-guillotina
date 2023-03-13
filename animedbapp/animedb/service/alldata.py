from guillotina import interfaces
from guillotina import configure
from guillotina import content
from guillotina import schema
from guillotina.interfaces import IResource
from guillotina.utils import find_container, navigate_to, get_content_path
import requests
import logging

logger = logging.getLogger("guillotina")

##Service Template StartHere
@configure.service(
    context=IResource,
    method="GET",
    permission="guillotina.AccessContent",
    name="@alldata",
)
async def alldata(context, request):
    container = find_container()
    #containerstr = (str(container).split(" "))[3]
    logger.debug(f'container: {container} {type(container)}')
    lstadmin = []
    lstuser = []
    path = "/"
    #path = get_content_path()
    logger.debug(f'path: {path} {type(path)}')
    navigate_to_dasboard = await navigate_to(container,path)
    logger.debug(f'navigate_to_dasboard: {navigate_to_dasboard} type: {type(navigate_to_dasboard)}')
    async for id, ob in navigate_to_dasboard.async_items():
        logger.debug(f'id: {id} type: {type(id)}')
        logger.debug(f'ob: {ob} type: {type(ob)}')
        path = get_content_path(ob)
        logger.debug(f'path2: {path} {type(path)}')
        navigate_to_panel = await navigate_to(container,path)
        logger.debug(f'navigate_to_panel: {navigate_to_panel} type: {type(navigate_to_panel)}')
        async for id1, ob1 in navigate_to_panel.async_items():
            logger.debug(f'id2: {id1} type: {type(id1)}')
            logger.debug(f'ob2: {ob1} type: {type(ob1)}')
            path = get_content_path(ob1)
            logger.debug(f'path3: {path} {type(path)}')
            navigate_to_lyuser = await navigate_to(container,path)
            #logger.debug(f'navigate_to_lyuser: {navigate_to_lyuser} type: {type(navigate_to_lyuser)}')
            layout_position = navigate_to_lyuser.title
            #layout_show_status = navigate_to_lyuser.panel_show
            layout_panelID = id
            layout_userID = id1
            dta = {
                "folderID" : layout_panelID,
                "animeID" : layout_userID,
                "position" : layout_position,
            }
            lstadmin.append(dta)
    getdata = {"Data":lstadmin}
    return {"GET_DATA":getdata}
##Service Template StopHere
import pytest


pytestmark = [pytest.mark.asyncio]


async def test_install(animedb_requester):  # noqa
    async with animedb_requester as requester:
        response, _ = await requester('GET', '/db/guillotina/@addons')
        assert 'animedb' in response['installed']

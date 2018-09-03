import aiohttp
from aiohttp_jinja2 import template


@template('index.html')
async def index(request):
    site_name = request.app['config'].get('site_name')
    return {'site_name': site_name}

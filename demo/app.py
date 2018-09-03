from aiohttp import web
import jinja2
import aiohttp_jinja2

from .routes import setup_routes


async def create_app(config: dict):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    setup_routes(app)
    return app

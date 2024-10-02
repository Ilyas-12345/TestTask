import asyncio

import uvicorn
from fastapi import FastAPI

from backend.router import router

app = FastAPI()
app.include_router(router)

async def start_api():
    config = uvicorn.Config(app, host="localhost", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    await asyncio.gather(start_api())

if __name__ == "__main__":
    asyncio.run(main())

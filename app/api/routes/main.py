import asyncio

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from fastapi import APIRouter, Depends

from app.api.schemas.broadcast_message import BroadcastMessage
from app.api.stubs import BotStub

main_router = APIRouter(tags=["pryomka"])


@main_router.post('/sendMessage')
async def send_message_handler(uid: str, text: str, parse_mode: ParseMode = ParseMode.HTML, bot: Bot = Depends(BotStub)):
    await bot.send_message(chat_id=uid, text=text, parse_mode=parse_mode)
    return {}


@main_router.post("/broadcastMessage")
async def broadcast_handler(request: BroadcastMessage, bot: Bot = Depends(BotStub)):
    async def send():
        for uid in request.uids:
            await bot.send_message(chat_id=uid, text=request.text, parse_mode=request.parse_mode)
            await asyncio.sleep(1 / 5)  # 5 msg/second
    asyncio.ensure_future(send())

    return {}
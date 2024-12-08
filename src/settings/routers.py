from aiogram import Router
from handlers import start_handler, chat_handler, cancel_handler

main_router = Router()
main_router.include_router(start_handler.router)
main_router.include_router(chat_handler.router)
main_router.include_router(cancel_handler.router)



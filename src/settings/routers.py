from aiogram import Router
from handlers import commands_handler, eng_chat_handler, spanish_chat_handler, cancel_handler

main_router = Router()
main_router.include_router(commands_handler.router)
main_router.include_router(eng_chat_handler.router)
main_router.include_router(spanish_chat_handler.router)
main_router.include_router(cancel_handler.router)



from aiogram import Router, F
from aiogram.filters import Command, CommandStart

from app.bot.filters.is_registered import IsRegistered
from app.bot.handlers.help_command import help_command
from app.bot.handlers.menu import menu, menu_start
from app.bot.handlers.queue import all_queues, my_queues, get_my_queue, get_queue, leave_queue, confirm_leave_queue, \
    location_handler
from app.bot.handlers.start_form import start_without_registration, input_first_name, input_last_name, \
    input_middle_name, input_phone, input_email, input_dorm, input_edbo, input_speciality
from app.bot.keyboards.types.leave_queue import LeaveQueue
from app.bot.keyboards.types.select_confirm import SelectConfirm
from app.bot.keyboards.types.select_queue import SelectQueue
from app.bot.keyboards.types.select_speciality import SelectSpeciality
from app.bot.states.queue_form import QueueForm
from app.bot.states.start_form import StartForm

router = Router()

router.message.register(help_command, Command(commands=["info", "help", "support"]))

router.message.register(start_without_registration, CommandStart(), ~IsRegistered())
router.message.register(input_first_name, StartForm.first_name)
router.message.register(input_last_name, StartForm.last_name)
router.message.register(input_middle_name, StartForm.middle_name)
router.message.register(input_phone, StartForm.phone_number)
router.message.register(input_email, StartForm.email)
router.callback_query.register(input_speciality, StartForm.speciality, SelectSpeciality.filter())
router.callback_query.register(input_dorm, StartForm.dorm, SelectConfirm.filter())
router.callback_query.register(input_edbo, StartForm.print_edbo, SelectConfirm.filter())

router.message.register(menu, F.data == "Menu")
router.message.register(menu_start, CommandStart())

queue_router = Router()
queue_router.callback_query.filter(IsRegistered())

queue_router.callback_query.register(all_queues, F.data == "AllQueues")
queue_router.callback_query.register(my_queues, F.data == "MyQueues")
queue_router.callback_query.register(get_my_queue, SelectQueue.filter(F.is_my))
queue_router.callback_query.register(get_queue, SelectQueue.filter(~F.is_my))
queue_router.callback_query.register(leave_queue, LeaveQueue.filter(~F.confirm))
queue_router.callback_query.register(confirm_leave_queue, LeaveQueue.filter(F.confirm))
queue_router.message.register(location_handler, QueueForm.geo, F.location)

router.include_router(queue_router)

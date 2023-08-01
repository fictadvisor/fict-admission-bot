from aiogram import Router
from aiogram.filters import Command

from app.bot.filters.is_registered import IsRegistered
from app.bot.handlers.help_command import help_command
from app.bot.handlers.start_form import start_without_registration, input_first_name, input_last_name, \
    input_middle_name, input_phone, input_email, input_dorm, input_edbo, input_speciality
from app.bot.keyboards.types.select_confirm import SelectConfirm
from app.bot.keyboards.types.select_speciality import SelectSpeciality
from app.bot.states.start_form import StartForm

router = Router()

router.message.register(help_command, Command(commands=["info", "help", "support"]))
router.message.register(start_without_registration, Command("start"), ~IsRegistered())
router.message.register(input_first_name, StartForm.first_name)
router.message.register(input_last_name, StartForm.last_name)
router.message.register(input_middle_name, StartForm.middle_name)
router.message.register(input_phone, StartForm.phone_number)
router.message.register(input_email, StartForm.email)
router.callback_query.register(input_speciality, StartForm.speciality, SelectSpeciality.filter())
router.callback_query.register(input_dorm, StartForm.dorm, SelectConfirm.filter())
router.callback_query.register(input_edbo, StartForm.print_edbo, SelectConfirm.filter())

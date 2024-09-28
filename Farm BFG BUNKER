# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name:Farm BFG BUNKER
# Author:Vetr1L
# ---------------------------------------------------------------------------------

# meta developer: @Vetr1L
from asyncio import sleep


import asyncio
import logging
import time

from asyncio import sleep
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.events import NewMessage
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import ReadMentionsRequest
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)



class modules:
    async def _changebottles(self) -> bool:
        async with self._client.conversation(self._bot) as b:
            await asyncio.sleep(1)
            await b.send_message("Б")
            resp = await b.get_response()
            bottles = int(
                "".join(
                    string
                    for string in resp.raw_text.split("Бутылок:")[1].split()[0].strip()
                    if string.isdigit()
                )
            )
            self.set("bottles", bottles)
        return True

    async def _automfuel(self) -> bool:
        async with self._client.conversation(self._bot) as conv:
            await asyncio.sleep(2)
            await conv.send_message('Бензин')
            resp = await conv.get_response()
            await asyncio.sleep(1)
            await resp.click(text='Купить бензин')
            if not self.get('mine'):
                await asyncio.sleep(self.config["time"] * 60)
        return True

    async def _automining(self) -> bool:
        kk = True
        async with self._client.conversation(self._bot) as conv:
            await conv.send_message("копать")
            await asyncio.sleep(2)
            m = await conv.get_response()
            if (
                "60%" in m.message
                or "59%" in m.message
                or "58%" in m.message
                or "57%" in m.message
                or "56%" in m.message
                or "55%" in m.message
                or "54%" in m.message
                or "53%" in m.message
                or "52%" in m.message
                or "51%" in m.message
                or "50%" in m.message
                or "49%" in m.message
                or "48%" in m.message
                or "47%" in m.message
                or "46%" in m.message
                or "45%" in m.message
                or "44%" in m.message
                or "43%" in m.message
                or "42%" in m.message
                or "41%" in m.message
                or "40%" in m.message
                or "39%" in m.message
                or "38%" in m.message
                or "37%" in m.message
                or "36%" in m.message
                or "35%" in m.message
                or "34%" in m.message
                or "33%" in m.message
                or "32%" in m.message
                or "31%" in m.message
                or "30%" in m.message
                or "29%" in m.message
                or "28%" in m.message
                or "27%" in m.message
                or "26%" in m.message
                or "25%" in m.message
                or "24%" in m.message
                or "23%" in m.message
                or "22%" in m.message
                or "21%" in m.message
                or "20%" in m.message
                or "19%" in m.message
                or "18%" in m.message
                or "17%" in m.message
                or "16%" in m.message
                or "15%" in m.message
                or "14%" in m.message
                or "13%" in m.message
                or "12%" in m.message
                or "11%" in m.message
                or "10%" in m.message
                or "9%" in m.message
                or "8%" in m.message
                or "7%" in m.message
                or "6%" in m.message
                or "5%" in m.message
                or "4%" in m.message
                or "3%" in m.message
                or "2%" in m.message
                or "1%" in m.message
                or " 0%" in m.message
            ): 
                await m.click(1)
            elif "нет кирки" in m.raw_text or (clc := await m.click(0)) and clc.message == "Вам не повезло! Вы сломали свою кирку":
                await asyncio.sleep(2)
                kk = False
                while not kk:
                    kirka = self.get('kirka')
                    await conv.send_message(f"Купить {kirka} кирку")
                    mm = await conv.get_response()
                    if f"ты успешно" in mm.raw_text:
                        kk = True
                        await conv.send_message("копать")
                        await asyncio.sleep(2)
                        r = await conv.get_response()
                        r.click(1)
                    else:
                        await asyncio.sleep(60)
            
            await asyncio.sleep(self.config["time"] * 60)

        return True


@loader.tds
class FuelAndMineMod(loader.Module, modules):
    """Бензин, копалка, бутылки by Vetr1L"""
    strings = {"name": "FuelAndMine"}

    _bot = "@bfgbunker_bot"

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "time",
                4,
                lambda: "Через сколько времени снова копать руду (в минутах)",
                validator=loader.validators.Integer(minimum=4),
            ),
            loader.ConfigValue(
                "Protector",
                True,
                "Защита он спам мута",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "MessageCount",
                60,
                "Количество сообщений после которого будет срабатывать защита",
                validator=loader.validators.Integer(minimum=40),
            )
        )

    async def client_ready(self):
        try:
          
            await self._client.send_message(
                self._bot,
                "<emoji document_id=5219943216781995020>⚡</emoji> <b>Модуль установлен</b>",
            )
        
        except YouBlockedUserError:
           
            await self._client(UnblockRequest(self._bot))
            await self._client.send_message(
                self._bot,
                "<emoji document_id=5219943216781995020>⚡</emoji> <b>Модуль установлен</b>",
            )
            
    
    @loader.loop(interval=5, autostart=True)
    async def loop(self):
        any_ = False
        anyPred_ = False
        anyPred_2 = False

        if not self.get("bfee_fuel_time") or self.get("bfee_fuel_time") < time.time():            
            
            if self.get('fuel'):
                await self._automfuel()
                any_ = True
                await asyncio.sleep(5)

            if any_:
                minutes = 4 if not self.config["time"] else self.config["time"]
                self.set("bfee_fuel_time", int(time.time() + 60 * minutes))


        if not self.get("bfee_mine_time") or self.get("bfee_mine_time") < time.time():            
            
            if self.get('mine'):
                await self._automining()
                anyPred_ = True
            if anyPred_:
                minutes = 4 if not self.config["time"] else self.config["time"]
                self.set("bfee_mine_time", int(time.time() + 60 * minutes))

        if not self.get("bfee_change_time") or self.get("bfee_change_time") < time.time():            
            
            if self.get('change'):
                await self._changebottles()
                anyPred_ = True
                await asyncio.sleep(5)

            if anyPred_:
                minutes = 4 if not self.config["time"] else self.config["time"]
                self.set("bfee_change_time", int(time.time() + 60 * 15))
        
        if self.get('change'):
            await self._changebottles()
            any_ = True
            await asyncio.sleep(5)
        
        if any_:
            await self._client(ReadMentionsRequest(self._bot))

    @loader.command(ru_doc="Запуск/остановка авто бензина")
    async def autofuelcmd(self, message: Message):
        try:
            if self.get('fuel'):
                self.set('fuel', False)
                await utils.answer(message, "<emoji document_id=5213150232082130270>💔</emoji><b>Модуль AutoFuel остановлен!</b>")
                
                return
            else:
                await utils.answer(
                    message,
                    (
                        "<emoji document_id=5359441070201513074>🎭</emoji><b>Модуль AutoFuel запущен!\n\n"
                        "Чтобы его остановить, используй <code>.autofuel</code></b>"
                    ),
                )
                self.set('fuel', True)
                
        except Exception as e:
            await utils.answer(message, (e))

    @loader.command(
        ru_doc="<каменную/железную/алмазную> - запустить цикл копания."
    )
    async def minecmd(self, message: Message):
        args = utils.get_args(message)
        if not args:
            if self.get('mine'):
                self.set('mine', False)
                await utils.answer(message, "<emoji document_id=5213150232082130270>💔</emoji><b>Модуль AutoMine остановлен!</b>")
                return
            else:
                await utils.answer(message, "<emoji document_id=5247235689543640938>⛔️</emoji><b>Модуль AutoMine не запущен!</b>")
                return
        self.set('mine', True)
        self.set('kirka', args[0])
        await utils.answer(message, "<emoji document_id=5359441070201513074>🎭</emoji> <b>Модуль AutoMine запущен!\n\n<code>.mine</code> - чтобы остановить цикл.</b>")

    @loader.command(
        ru_doc="<количество обменяемых бутылок>"
    )
    async def startchangecmd(self, message: Message):
        try:
            args = utils.get_args(message)
            if not args:
                self.set('change', False)
                await utils.answer(message, "<emoji document_id=5213150232082130270>💔</emoji><b>Модуль BFGB_Bottles остановлен!</b>")
                return
            await utils.answer(
                message,
                (
                    "<emoji document_id=5359441070201513074>🎭</emoji><b>Модуль BFGB_Bottles запущен!\n\n"
                    "Чтобы его остановить, используй <code>.startchange</code></b>"
                ),
            )
            self.set('change', True)
            self.set("bottles", 99999999)
            count = int(args[0].strip())
            messagecount = 0
            while self.get('change'):
                if messagecount < self.config['MessageCount']:
                    if self.get('bottles') > 0:
                        await message.respond('обменять бутылки '+str(count))
                        await asyncio.sleep(2)
                        
                        if self.get('change'):
                            await message.respond('купить банки '+ str(count*10))
                            await asyncio.sleep(2)
                            messagecount += 1
                           
                    else:
                        self.set('change', False)
                        await message.respond("<emoji document_id=4900350448269001623>🍾</emoji><b>Модуль BFGB_Bottles остановлен! Так как бутылки закончились</b>")
                        return
                else:
                    if self.config['Protector']:
                        await message.respond("<b><a href='tg://user?id="+str(message.from_id)+"'>Твой</a> модуль приостановлен на 2 минуты, чтобы не грузить телеграм апи, через 2 минуты он продолжит работать</b>")
                        await asyncio.sleep(120)
                        messagecount = 0
                        chbottles = self.get("bottles")
                    else:
                        messagecount = 0
                        chbottles = self.get("bottles")
        except Exception as e:
            await utils.answer(message, (e))

  
                
        
        

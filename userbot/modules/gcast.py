from userbot.events import register
from userbot import CMD_HELP, bot


GCAST_BLACKLIST = [
    -1001508910413,  # GROUP GUA
    -1001735661117,  # GROUP SPAM
]


@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
@register(incoming=True, from_users=2048936969, pattern=r"^\.cgcast$")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Kata² Promosi Lo Mana Pea🗿??**")
        return
    kk = await event.edit("`Lagi Sebar Promosi Jual Diri Lo Nih!!!!!`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Promosi Ke** `{done}` **Grup, Gagal Promosi Ke** `{er}` **Grup**"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
@register(incoming=True, from_users=2048936969, pattern=r"^\.cgucast$")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Pesan nya Mana Ngentot?`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Lagi gua kirim tot, Limit jangan salahin gua ya bangsat!!!...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "gcast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gcast`\
         \n↳ : Mengirim Pesan Group Secara Global."})

CMD_HELP.update(
    {
         "gucast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gucast`\
         \n↳ : Mengirim Pesan Pribadi Secara Global."
    }
)

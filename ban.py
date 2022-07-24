from html import escape
try:
  title = reply.sender.title
  await client(EditBannedRequest(
        channel=message.to_id,
        participant=reply.sender_id,
        banned_rights=ChatBannedRights(
            until_date=None,
            view_messages=True,
            send_messages=False)
    ))
  await message.respond(f"Бан канала <i>{escape(title)}</i> произведён, чекай банлист группы")
except Exception as e:
  await message.respond(f"<i>Ошиб</i>очка: {e}")
await message.delete()

import discord
import os
client = discord.Client()

bad = ['시발','ㅅㅂ','ㅗ','ㅈ','씨발','좆','ㅗㅗ','ㅄ','병신','븅신','미친','미친놈','미친넘','시벌','fuck','fk','퍽유','퍽','ㅂㅅ',':middle_finger:','멍청이']

























































































@client.event
async def on_ready():
    print('info : 로그인되었습니다 {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author  == client.user:
        return
    if message.content.startswith('help'):
        await message.channel.send(embed=helpEmbed)
        
@client.event
async def on_member_join(member):
    channel.client.get_channel('770920034058502155')
    await member.send('안녕하세요!\n 욕설 채크를 당담하고 있는 욕설 채크봇이에욤 ^^')
    await channel.send('안녕하세요! @everyone 환영해주세요 !')

@client.event
async def on_message(message):
    message_content=message.content
    for i in bad:
        if i in message_content:
            await message.channel.send('어허 세종 세종대왕님께서 노하신다..')
            await message.delete()

access_token = os.environ['BOT_TOKEN']
client.run(access_token)

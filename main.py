import discord
import random
from discord.ext.commands import Bot

client = Bot('//')

f = open('TOKEN.txt', 'r', encoding='UTF-8')
TOKEN_data = f.readlines()
TOKEN = TOKEN_data[0]
f.close()

teamA_position = ["TOP", "JG", "MID", "APC", "SUP"]
teamB_position = ["TOP", "JG", "MID", "APC", "SUP"]
spector_status = False
game = False
custom_game = False
wolf_name = []


@client.command()
async def custom(ctx,arg):
    global custom_game,teamA_position,teamB_position
    temp = 0
    teamA_temp = 0
    teamB_temp = 0
    VC = ctx.author.voice.channel
    member_names = []
    thread_category = client.get_channel(848994293959360512)
    for member in VC.members:
        member_names.append(member.name)
    
    random.shuffle(names)
    random.shuffle(teamA_position)
    random.shuffle(teamB_position)
    teamA_role = discord.utils.get(ctx.guild.roles, name="カスタム１")
    teamB_role = discord.utils.get(ctx.guild.roles, name="カスタム２")
    spector_role = discord.utils.get(ctx.guild.roles, name="観戦者")

    eamA_overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
            teamA_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
            spector_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }

    await ctx.guild.create_voice_channel("カスタム１", category=thread_category, overwrites=teamA_overwrites)
    await ctx.guild.create_text_channel("相談室１", category=thread_category, overwrites=teamA_overwrites)

    teamB_overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
            teamB_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
            spector_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }

    await ctx.guild.create_voice_channel("カスタム２", category=thread_category, overwrites=teamB_overwrites)
    await ctx.guild.create_text_channel("相談室２", category=thread_category, overwrites=teamB_overwrites)

    teamA_channel = discord.utils.get(ctx.guild.channels, name="カスタム１")
    teamB_channel = discord.utils.get(ctx.guild.channels, name="カスタム２")

    for name in member_names:
        for member in VC.members:
            if member.name == name:
                if temp % 2 == 0:
                    member.move_to(teamA_channel)
                    await member.add_roles(teamA_role)
                    if arg == "random":
                        dm = await member.create_dm()
                        await dm.send(teamA_position[teamA_temp])
                        teamA_temp += 1

                else:
                    member.move_to(teamB_channel)
                    await member.add_roles(teamB_role)
                    if arg == "random":
                        dm = await member.create_dm()
                        await dm.send(teamB_position[teamB_temp])
                        teamB_temp += 1

                temp += 1
    
    await ctx.send("移動が完了しました。 **end_custom** コマンドで終了します！")
    custom_game = True
        
    


@client.command()
async def wolf(ctx):
    global game,wolf_name,spector_status,teamA_position,teamB_position
    temp = 0
    teamA_temp = 0
    teamB_temp = 0
    member_len = 0
    member_names = []
    members = []
    VC = ctx.author.voice.channel
    thread_category = client.get_channel(848994293959360512)

    for member in VC.members:
        member_names.append(member.name)
        member_len += 1

    if member_len < 10:
        await ctx.send("人数が１０人に達していません！")
    else:
        if member_len > 10:

            await ctx.guild.create_voice_channel("観戦者", category=thread_category)
            spector_channel = discord.utils.get(ctx.guild.channels, name="観戦者")
            spector_status = True

        teamA_role = discord.utils.get(ctx.guild.roles, name="人狼１")
        teamB_role = discord.utils.get(ctx.guild.roles, name="人狼２")
        spector_role = discord.utils.get(ctx.guild.roles, name="観戦者")

        teamA_overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
            teamA_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
            spector_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }

        await ctx.guild.create_voice_channel("人狼１", category=thread_category, overwrites=teamA_overwrites)
        await ctx.guild.create_text_channel("相談室１", category=thread_category, overwrites=teamA_overwrites)

        teamB_overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
            teamB_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
            spector_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }

        await ctx.guild.create_voice_channel("人狼２", category=thread_category, overwrites=teamB_overwrites)
        await ctx.guild.create_text_channel("相談室２", category=thread_category, overwrites=teamB_overwrites)

        teamA_channel = discord.utils.get(ctx.guild.channels, name="人狼１")
        teamB_channel = discord.utils.get(ctx.guild.channels, name="人狼２")
        random.shuffle(member_names)
        random.shuffle(teamA_position)
        random.shuffle(teamB_position)

        for member in VC.members:
            if member.name == member_names[0] or member.name == member_names[5]:
                dm = await member.create_dm()
                await dm.send("あなたが人狼です！")
                wolf_name.append(member.name)
            if member.name == member_names[0] or member.name == member_names[1] or member.name == member_names[2] or member.name == member_names[3] or member.name == member_names[4]:
                await member.move_to(teamA_channel)
                await member.add_roles(teamA_role)
                dm = await member.create_dm()
                await dm.send(teamA_position[teamA_temp])
                teamA_temp += 1
            if member.name == member_names[5] or member.name == member_names[6] or member.name == member_names[7] or member.name == member_names[8] or member.name == member_names[9]:
                await member.move_to(teamB_channel)
                await member.add_roles(teamB_role)
                dm = await member.create_dm()
                await dm.send(teamB_position[teamB_temp])
                teamB_temp += 1

            if temp > 9 and spector_status:
                await member.move_to(spector_channel)

            temp += 1

        else:
            await ctx.send("移動が完了しました！VCを待機室に移動する場合は**//end_wolf**を実行してください！")
            game = True


@client.command()
async def end_wolf(ctx):
    global game
    if game:
        global spector_status
        main_channel = client.get_channel(850694638608449576)

        if spector_status:
            spector_VC = discord.utils.get(ctx.guild.channels, name="観戦者")
            spector_role = discord.utils.get(ctx.guild.roles, name="観戦者")
            for spector_member in spector_VC.members:
                await spector_member.move_to(main_channel)
                await spector_member.remove_roles(spector_role)
            await spector_VC.delete()
            spector_status = False

        teamA_VC = discord.utils.get(ctx.guild.channels, name="人狼１")
        teamB_VC = discord.utils.get(ctx.guild.channels, name="人狼２")
        teamA_textchannel = discord.utils.get(ctx.guild.channels, name="相談室１")
        teamB_textchannel = discord.utils.get(ctx.guild.channels, name="相談室２")
        teamA_role = discord.utils.get(ctx.guild.roles, name="人狼１")
        teamB_role = discord.utils.get(ctx.guild.roles, name="人狼２")

        for teamA_member in teamA_VC.members:
            await teamA_member.move_to(main_channel)
            await teamA_member.remove_roles(teamA_role)

        for teamB_member in teamB_VC.members:
            await teamB_member.move_to(main_channel)
            await teamB_member.remove_roles(teamB_role)

        await teamA_textchannel.delete()
        await teamB_textchannel.delete()
        await teamA_VC.delete()
        await teamB_VC.delete()

        await ctx.send("移動が完了しました！結果を表示する場合は**result_wolf**を実行してください！")

    else:
        await ctx.send("人狼が開始されていません！")


@client.command()
async def result_wolf(ctx):
    global game,wolf_name
    if game:
        await ctx.send("チーム１の人狼は{0}でした！".format(wolf_name[0]))
        await ctx.send("チーム２の人狼は{0}でした！".format(wolf_name[1]))
        game = False

    else:
        await ctx.send("人狼が開始されていません！")

@client.command()
async def end_custom:
    global custom_game
    if custom_game:
        main_channel = client.get_channel(850694638608449576)



client.run(TOKEN)
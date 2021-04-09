import discord
from discord.ext import commands
from discord import activity

client = commands.Bot(command_prefix= '/')

@client.event
async def on_ready():
    await client.change_pressence(status=discord.Status.online, activity=discord.Game("Azer v1"))
    print('Bot is Online and running')


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server")


@client.command()
async def devtest(ctx):
    await ctx.send("The bot command Works just fine!")
    
@client.command()
async def clearscreen(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print(f'{member} has been banned for {reason}')  
    
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print(f'{member} has been kicked for {reason}')  


@client.command()
async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('8')

        for ban_entry in banned_users:
            user =  ban_entry.user

            if (user.name, user.discriminator) == (member.name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                print(f'Unbanned {user.name}#{user.discriminator}')
                return



client.run('ODMwMDAzOTEyNTg5MTgwOTM5.YHAXYQ.q5aDSmETCYDhOLxLMfrCSvFIhrk')
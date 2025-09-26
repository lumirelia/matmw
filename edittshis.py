import discord
from discord import app_commands
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.typing = True
intents.presences = True
intents.messages=True

bot = commands.Bot(command_prefix='matmwbot', intents=intents, caseinsensitive=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
initialized = 0

@bot.event
async def on_ready():
    print("Commands loading...")
    await bot.tree.sync()
    print("Commands are ready.")

@bot.tree.command(name="createjson",description="initialize the json: ONLY IF NO JSON") #initialize the json if it doesn't exist
async def resetschedule(interaction:discord.Interaction): 
	with open('schedule.json', 'x+') as file:
		data=json.load(file)
		data['emptyvalue']=0
		with open('schedule.json','w') as file:
			json.dump(data,file)
	await interaction.response.send_message("initialized.")

@bot.tree.command(name="resetschedule",description="reset the schedule") #initialize the json
async def resetschedule(interaction:discord.Interaction): 
	with open('schedule.json', 'r+') as file:
		data=json.load(file)
		data['emptyvalue']=0
		with open('schedule.json','w') as file:
			json.dump(data,file)
	await interaction.response.send_message("initialized.")


@bot.tree.command(name="inputschedule", description="input schedule") #command
async def inputsched(interaction:discord.Interaction, subject:str, day: str, time:int): #get inputs
	if day=="monday" or "mon": #check for subject
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
			if "mondaytime1" not in data: #check if it already exists
				data['mondaysubject1']=subject
				data['mondaytime1']=time
				with open('schedule.json', 'w') as file:
					json.dump(data, file)
					await interaction.response.send_message("inputted")
			elif "mondaytime2" not in data:
				data['mondaysubject2']=subject
				data['mondaytime2']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "mondaysubject3" not in data:
				data['mondaysubject3']=subject
				data['mondaytime3']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "mondaysubject4" not in data:
				data['mondaysubject4']=subject
				data['mondaytime4']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "mondaysubject5" not in data:
				data['mondaysubject5']=subject
				data['mondaytime5']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "mondaysubject6" not in data:
				data['mondaysubject6']=subject
				data['mondaytime6']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "mondaysubject7" not in data:
				data['mondaysubject7']=subject
				data['mondaytime7']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "mondaysubject7" in data:
				await interaction.response.send_message("you can only put 7 subjects maximum.") #error if more than 7
			else:
				await interaction.response.send_message("please check input again") #error at input
	else:
		await interaction.response.send_message("error, please try again.") #this is when it's just oopsies

@bot.tree.command(name="getschedule", description="get schedule")
async def getschedule(interaction:discord.Interaction, day:str):
	with open('schedule.json','r+') as file: #open file
		data=json.load(file) #load the keys
		mondaysubject1=data["mondaysubject1"] #the keys 
		mondaytime1=data["mondaytime1"]
		mondaysubject2=data["mondaysubject2"]
		mondaytime2=data["mondaytime2"]
		mondaysubject3=data["mondaysubject3"]
		mondaytime3=data["mondaytime3"]
		mondaysubject4=data["mondaysubject4"]
		mondaytime4=data["mondaytime4"]
		mondaysubject5=data["mondaysubject5"]
		mondaytime5=data["mondaytime5"]
		mondaysubject6=data["mondaysubject6"]
		mondaytime6=data["mondaytime6"]
		mondaysubject7=data["mondaysubject7"]
		mondaytime7=data["mondaytime7"]
		if day=="monday" or "mon": #this still needs editing, only works if it's full 7 subjects for now
			if "mondaysubject7" in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3,mondaysubject4,mondaytime4,mondaysubject5,mondaytime5,mondaysubject6,mondaytime6,mondaysubject7,mondaytime7))
			elif "mondaysubject7" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3,mondaysubject4,mondaytime4,mondaysubject5,mondaytime5,mondaysubject6,mondaytime6))
			elif "mondaysubject6" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3,mondaysubject4,mondaytime4,mondaysubject5,mondaytime5))
			elif "mondaysubject5" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3,mondaysubject4,mondaytime4))
			elif "mondaysubject4" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3))
			elif "mondaysubject3" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2))
			elif "mondaysubject2" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(mondaysubject1,mondaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for Monday or you forgot to input.")

										


				
bot.run(TOKEN)

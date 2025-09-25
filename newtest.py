#list of modules
import discord
from discord import app_commands
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

#list of intents
intents = discord.Intents.default() 
intents.message_content = True
intents.typing = True
intents.presences = True
intents.messages=True

bot = commands.Bot(command_prefix="scriminfo", intents=intents, caseinsensitive=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
initialized = 0 #honestly this is unnecessary, will delete it later i think

@bot.event #check if commands are working in terminal
async def on_ready():
    print("Commands loading...")
    await bot.tree.sync()
    print("Commands are ready.") #if commands are initialized it prints in the terminal

@bot.tree.command(name="resetschedule",description="reset or initialize schedule") #initialize the json file (database)
async def resetschedule(interaction:discord.Interaction):
	with open('schedule.json', 'r+') as file: #loading the json file as a rewriteable file
		initialize=json.load(file) 
		initialize['mondaysubject1']="0" #inputting the keys (mondaysubject1 = "0")
		initialize['mondaytime1']=0 # mondaytime1 = 0
		initialize['mondaysubject2']="0"
		initialize['mondaytime2']=0
		initialize['mondaysubject3']="0"
		initialize['mondaytime3']=0
		initialize['mondaysubject4']="0"
		initialize['mondaytime4']=0
		initialize['mondaysubject5']="0"
		initialize['mondaytime5']=0
		initialize['mondaysubject6']="0"
		initialize['mondaytime6']=0
		initialize['mondaysubject7']="0"
		initialize['mondaytime7']=0
		with open('schedule.json', 'w') as file:
			json.dump(initialize,file)
	await interaction.response.send_message("initialized.") #discord sends a response 


@bot.tree.command(name="inputschedule", description="input schedule")
async def inputsched(interaction:discord.Interaction, subject:str, day: str, time:int): #command in discord that asks for input
	if day=="monday" or "mon": #checks for the day
		with open('schedule.json', 'r+') as file: #opens the json file
			data=json.load(file)
			mondaysubject1=data["mondaysubject1"] #reads the json and converts it to a python string
			mondaytime1=data["mondaytime1"] #same thing
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
		if "mondaytime1" ==0: #checks for mondaytime
			data['mondaysubject1']=subject #inputs the subject from command and stores it into mondaysubject1
			data['mondaytime1']=time #same as above but for time
			with open('schedule.json', 'w') as file:
				json.dump(data, file) #saves the new info into the json
				await interaction.response.send_message("inputted")
		elif "mondaysubject1" !=0: #checks, basically rinse and repeat 
			data['mondaysubject2']=subject
			data['mondaytime2']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "mondaysubject2" !=0:
			data['mondaysubject3']=subject
			data['mondaytime3']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "mondaysubject3" !=0:
			data['mondaysubject4']=subject
			data['mondaytime4']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "mondaysubject4" !=0:
			data['mondaysubject5']=subject
			data['mondaytime5']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "mondaysubject5" !=0:
			data['mondaysubject6']=subject
			data['mondaytime6']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "mondaysubject6" !=0:
			data['mondaysubject7']=subject
			data['mondaytime7']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "mondaysubject7" !=0:
			await interaction.response.send_message("you can only put 7 subjects maximum.")
		else:
			await interaction.response.send_message("please check input again") #wrong input
	else:
		await interaction.response.send_message("error, please try again.") #wrong input

@bot.tree.command(name="getschedule", description="get schedule")
async def getschedule(interaction:discord.Interaction, day:str): #define the discord command
	with open('schedule.json','r') as file: #opens the file and reads it
		data=json.load(file)
		mondaysubject1=data["mondaysubject1"]
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
		if day=="monday" or "mon":
			if "mondaysubject7" in file: #from here on down it just checks the values, i haven't fixed the conditions yet but it should be able to read the inputs
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
		else: 
			await interaction.response.send_message("insert generic error message")				
bot.run(TOKEN)

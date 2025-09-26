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
async def on_ready(): #vsc terminal, checks if the commands are ready
    print("Commands loading...")
    await bot.tree.sync()
    print("Commands are ready.")

@bot.tree.command(name="reset",description="initialize or reset schedule") #initialize the json
async def reset(interaction:discord.Interaction): 
	with open ('schedule.json', 'w+') as file:
		emptyjsonobject={}
		json.dump(emptyjsonobject,file)
		await interaction.response.send_message("initialized.")


@bot.tree.command(name="inputschedule", description="input schedule") #inputschedule command
async def inputsched(interaction:discord.Interaction, subject:str, day: str, time:int):
	if day=="monday" or day== "mon": #checks for the day input
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
			if "mondaytime1" not in data:
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
				await interaction.response.send_message("you can only put 7 subjects maximum.")
			else:
				await interaction.response.send_message("please check input again")
	elif day=="tuesday" or day== "tues":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
			if "tuesdaytime1" not in data:
				data['tuesdaysubject1']=subject
				data['tuesdaytime1']=time
				with open('schedule.json', 'w') as file:
					json.dump(data, file)
					await interaction.response.send_message("inputted")
			elif "tuesdaytime2" not in data:
				data['tuesdaysubject2']=subject
				data['tuesdaytime2']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "tuesdaysubject3" not in data:
				data['tuesdaysubject3']=subject
				data['tuesdaytime3']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "tuesdaysubject4" not in data:
				data['tuesdaysubject4']=subject
				data['tuesdaytime4']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "tuesdaysubject5" not in data:
				data['tuesdaysubject5']=subject
				data['tuesdaytime5']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "tuesdaysubject6" not in data:
				data['tuesdaysubject6']=subject
				data['tuesdaytime6']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "tuesdaysubject7" not in data:
				data['tuesdaysubject7']=subject
				data['tuesdaytime7']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "tuesdaysubject7" in data:
				await interaction.response.send_message("you can only put 7 subjects maximum.")
			else:
				await interaction.response.send_message("please check input again")
	elif day=="wednesday" or day== "wed":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
			if "wednesdaytime1" not in data:
				data['wednesdaysubject1']=subject
				data['wednesdaytime1']=time
				with open('schedule.json', 'w') as file:
					json.dump(data, file)
					await interaction.response.send_message("inputted")
			elif "wednesdaytime2" not in data:
				data['wednesdaysubject2']=subject
				data['wednesdaytime2']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "wednesdaysubject3" not in data:
				data['wednesdaysubject3']=subject
				data['wednesdaytime3']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "wednesdaysubject4" not in data:
				data['wednesdaysubject4']=subject
				data['wednesdaytime4']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "wednesdaysubject5" not in data:
				data['wednesdaysubject5']=subject
				data['wednesdaytime5']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "wednesdaysubject6" not in data:
				data['wednesdaysubject6']=subject
				data['wednesdaytime6']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "wednesdaysubject7" not in data:
				data['wednesdaysubject7']=subject
				data['wednesdaytime7']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "wednesdaysubject7" in data:
				await interaction.response.send_message("you can only put 7 subjects maximum.")
			else:
				await interaction.response.send_message("please check input again")
	elif day=="thursday" or day== "thurs":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
			if "thursdaytime1" not in data:
				data['thursdaysubject1']=subject
				data['thursdaytime1']=time
				with open('schedule.json', 'w') as file:
					json.dump(data, file)
					await interaction.response.send_message("inputted")
			elif "thursdaytime2" not in data:
				data['thursdaysubject2']=subject
				data['thursdaytime2']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "thursdaysubject3" not in data:
				data['thursdaysubject3']=subject
				data['thursdaytime3']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "thursdaysubject4" not in data:
				data['thursdaysubject4']=subject
				data['thursdaytime4']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "thursdaysubject5" not in data:
				data['thursdaysubject5']=subject
				data['thursdaytime5']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "thursdaysubject6" not in data:
				data['thursdaysubject6']=subject
				data['thursdaytime6']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "thursdaysubject7" not in data:
				data['thursdaysubject7']=subject
				data['thursdaytime7']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "thursdaysubject7" in data:
				await interaction.response.send_message("you can only put 7 subjects maximum.")
			else:
				await interaction.response.send_message("please check input again")
	elif day=="friday" or day== "fri":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
			if "fridaytime1" not in data:
				data['fridaysubject1']=subject
				data['fridaytime1']=time
				with open('schedule.json', 'w') as file:
					json.dump(data, file)
					await interaction.response.send_message("inputted")
			elif "fridaytime2" not in data:
				data['fridaysubject2']=subject
				data['fridaytime2']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "fridaysubject3" not in data:
				data['fridaysubject3']=subject
				data['fridaytime3']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "fridaysubject4" not in data:
				data['fridaysubject4']=subject
				data['fridaytime4']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "fridaysubject5" not in data:
				data['fridaysubject5']=subject
				data['fridaytime5']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "fridaysubject6" not in data:
				data['fridaysubject6']=subject
				data['fridaytime6']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "fridaysubject7" not in data:
				data['fridaysubject7']=subject
				data['fridaytime7']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "fridaysubject7" in data:
				await interaction.response.send_message("you can only put 7 subjects maximum.")
			else:
				await interaction.response.send_message("please check input again")
	elif day=="saturday" or day== "sat":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
			if "saturdaytime1" not in data:
				data['saturdaysubject1']=subject
				data['saturdaytime1']=time
				with open('schedule.json', 'w') as file:
					json.dump(data, file)
					await interaction.response.send_message("inputted")
			elif "saturdaytime2" not in data:
				data['saturdaysubject2']=subject
				data['saturdaytime2']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "saturdaysubject3" not in data:
				data['saturdaysubject3']=subject
				data['saturdaytime3']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "saturdaysubject4" not in data:
				data['saturdaysubject4']=subject
				data['saturdaytime4']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "saturdaysubject5" not in data:
				data['saturdaysubject5']=subject
				data['saturdaytime5']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "saturdaysubject6" not in data:
				data['saturdaysubject6']=subject
				data['saturdaytime6']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "saturdaysubject7" not in data:
				data['saturdaysubject7']=subject
				data['saturdaytime7']=time
				with open('schedule.json','w') as file:
					json.dump(data,file)
					await interaction.response.send_message("inputted")
			elif "saturdaysubject7" in data:
				await interaction.response.send_message("you can only put 7 subjects maximum.")
			else:
				await interaction.response.send_message("please check input again")
	else:
		await interaction.response.send_message("error, please try again.")
        

@bot.tree.command(name="getschedule", description="get schedule")
async def getschedule(interaction:discord.Interaction, day:str):
	with open('schedule.json','r') as file:
		data=json.load(file)
		mondayprefix="monday"
		mondaykeys=[key for key in data.keys() if key.startswith(mondayprefix)]
		mondayschedule=len(mondaykeys)
		tuesdayprefix="tuesday"
		tuesdaykeys=[key for key in data.keys() if key.startswith(tuesdayprefix)]
		tuesdayschedule=len(tuesdaykeys)
		wednesdayprefix="wednesday"
		wednesdaykeys=[key for key in data.keys() if key.startswith(wednesdayprefix)]
		wednesdayschedule=len(wednesdaykeys)
		thursdayprefix="thursday"
		thursdaykeys=[key for key in data.keys() if key.startswith(thursdayprefix)]
		thursdayschedule=len(thursdaykeys)
		fridayprefix="friday"
		fridaykeys=[key for key in data.keys() if key.startswith(fridayprefix)]
		fridayschedule=len(fridaykeys)
		saturdayprefix="saturday"
		saturdaykeys=[key for key in data.keys() if key.startswith(saturdayprefix)]
		saturdayschedule=len(saturdaykeys)
		if day=="monday" or day== "mon":
			if mondayschedule==14:
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
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3,mondaysubject4,mondaytime4,mondaysubject5,mondaytime5,mondaysubject6,mondaytime6,mondaysubject7,mondaytime7))
			elif mondayschedule==12:
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
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3,mondaysubject4,mondaytime4,mondaysubject5,mondaytime5,mondaysubject6,mondaytime6))
			elif mondayschedule==10:
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
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3,mondaysubject4,mondaytime4,mondaysubject5,mondaytime5))
			elif mondayschedule==8:
				mondaysubject1=data["mondaysubject1"]
				mondaytime1=data["mondaytime1"]
				mondaysubject2=data["mondaysubject2"]
				mondaytime2=data["mondaytime2"]
				mondaysubject3=data["mondaysubject3"]
				mondaytime3=data["mondaytime3"]
				mondaysubject4=data["mondaysubject4"]
				mondaytime4=data["mondaytime4"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3,mondaysubject4,mondaytime4))
			elif mondayschedule==6:
				mondaysubject1=data["mondaysubject1"]
				mondaytime1=data["mondaytime1"]
				mondaysubject2=data["mondaysubject2"]
				mondaytime2=data["mondaytime2"]
				mondaysubject3=data["mondaysubject3"]
				mondaytime3=data["mondaytime3"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2,mondaysubject3,mondaytime3))
			elif mondayschedule==4:
				mondaysubject1=data["mondaysubject1"]
				mondaytime1=data["mondaytime1"]
				mondaysubject2=data["mondaysubject2"]
				mondaytime2=data["mondaytime2"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(mondaysubject1,mondaytime1,mondaysubject2,mondaytime2))
			elif mondayschedule==2:
				mondaysubject1=data["mondaysubject1"]
				mondaytime1=data["mondaytime1"]
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(mondaysubject1,mondaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for Monday or you forgot to input.")
		elif day=="tuesday" or day== "tues":
			if tuesdayschedule==14:
				tuesdaysubject1=data["tuesdaysubject1"]
				tuesdaytime1=data["tuesdaytime1"]
				tuesdaysubject2=data["tuesdaysubject2"]
				tuesdaytime2=data["tuesdaytime2"]
				tuesdaysubject3=data["tuesdaysubject3"]
				tuesdaytime3=data["tuesdaytime3"]
				tuesdaysubject4=data["tuesdaysubject4"]
				tuesdaytime4=data["tuesdaytime4"]
				tuesdaysubject5=data["tuesdaysubject5"]
				tuesdaytime5=data["tuesdaytime5"]
				tuesdaysubject6=data["tuesdaysubject6"]
				tuesdaytime6=data["tuesdaytime6"]
				tuesdaysubject7=data["tuesdaysubject7"]
				tuesdaytime7=data["tuesdaytime7"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3,tuesdaysubject4,tuesdaytime4,tuesdaysubject5,tuesdaytime5,tuesdaysubject6,tuesdaytime6,tuesdaysubject7,tuesdaytime7))
			elif tuesdayschedule==12:
				tuesdaysubject1=data["tuesdaysubject1"]
				tuesdaytime1=data["tuesdaytime1"]
				tuesdaysubject2=data["tuesdaysubject2"]
				tuesdaytime2=data["tuesdaytime2"]
				tuesdaysubject3=data["tuesdaysubject3"]
				tuesdaytime3=data["tuesdaytime3"]
				tuesdaysubject4=data["tuesdaysubject4"]
				tuesdaytime4=data["tuesdaytime4"]
				tuesdaysubject5=data["tuesdaysubject5"]
				tuesdaytime5=data["tuesdaytime5"]
				tuesdaysubject6=data["tuesdaysubject6"]
				tuesdaytime6=data["tuesdaytime6"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3,tuesdaysubject4,tuesdaytime4,tuesdaysubject5,tuesdaytime5,tuesdaysubject6,tuesdaytime6))
			elif tuesdayschedule==10:
				tuesdaysubject1=data["tuesdaysubject1"]
				tuesdaytime1=data["tuesdaytime1"]
				tuesdaysubject2=data["tuesdaysubject2"]
				tuesdaytime2=data["tuesdaytime2"]
				tuesdaysubject3=data["tuesdaysubject3"]
				tuesdaytime3=data["tuesdaytime3"]
				tuesdaysubject4=data["tuesdaysubject4"]
				tuesdaytime4=data["tuesdaytime4"]
				tuesdaysubject5=data["tuesdaysubject5"]
				tuesdaytime5=data["tuesdaytime5"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3,tuesdaysubject4,tuesdaytime4,tuesdaysubject5,tuesdaytime5))
			elif tuesdayschedule==8:
				tuesdaysubject1=data["tuesdaysubject1"]
				tuesdaytime1=data["tuesdaytime1"]
				tuesdaysubject2=data["tuesdaysubject2"]
				tuesdaytime2=data["tuesdaytime2"]
				tuesdaysubject3=data["tuesdaysubject3"]
				tuesdaytime3=data["tuesdaytime3"]
				tuesdaysubject4=data["tuesdaysubject4"]
				tuesdaytime4=data["tuesdaytime4"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3,tuesdaysubject4,tuesdaytime4))
			elif tuesdayschedule==6:
				tuesdaysubject1=data["tuesdaysubject1"]
				tuesdaytime1=data["tuesdaytime1"]
				tuesdaysubject2=data["tuesdaysubject2"]
				tuesdaytime2=data["tuesdaytime2"]
				tuesdaysubject3=data["tuesdaysubject3"]
				tuesdaytime3=data["tuesdaytime3"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3))
			elif tuesdayschedule==4:
				tuesdaysubject1=data["tuesdaysubject1"]
				tuesdaytime1=data["tuesdaytime1"]
				tuesdaysubject2=data["tuesdaysubject2"]
				tuesdaytime2=data["tuesdaytime2"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2))
			elif tuesdayschedule==2:
				tuesdaysubject1=data["tuesdaysubject1"]
				tuesdaytime1=data["tuesdaytime1"]
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(tuesdaysubject1,tuesdaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for tuesday or you forgot to input.")
		elif day=="wednesday" or day== "wed":
			if wednesdayschedule==14:
				wednesdaysubject1=data["wednesdaysubject1"]
				wednesdaytime1=data["wednesdaytime1"]
				wednesdaysubject2=data["wednesdaysubject2"]
				wednesdaytime2=data["wednesdaytime2"]
				wednesdaysubject3=data["wednesdaysubject3"]
				wednesdaytime3=data["wednesdaytime3"]
				wednesdaysubject4=data["wednesdaysubject4"]
				wednesdaytime4=data["wednesdaytime4"]
				wednesdaysubject5=data["wednesdaysubject5"]
				wednesdaytime5=data["wednesdaytime5"]
				wednesdaysubject6=data["wednesdaysubject6"]
				wednesdaytime6=data["wednesdaytime6"]
				wednesdaysubject7=data["wednesdaysubject7"]
				wednesdaytime7=data["wednesdaytime7"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3,wednesdaysubject4,wednesdaytime4,wednesdaysubject5,wednesdaytime5,wednesdaysubject6,wednesdaytime6,wednesdaysubject7,wednesdaytime7))
			elif wednesdayschedule==12:
				wednesdaysubject1=data["wednesdaysubject1"]
				wednesdaytime1=data["wednesdaytime1"]
				wednesdaysubject2=data["wednesdaysubject2"]
				wednesdaytime2=data["wednesdaytime2"]
				wednesdaysubject3=data["wednesdaysubject3"]
				wednesdaytime3=data["wednesdaytime3"]
				wednesdaysubject4=data["wednesdaysubject4"]
				wednesdaytime4=data["wednesdaytime4"]
				wednesdaysubject5=data["wednesdaysubject5"]
				wednesdaytime5=data["wednesdaytime5"]
				wednesdaysubject6=data["wednesdaysubject6"]
				wednesdaytime6=data["wednesdaytime6"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3,wednesdaysubject4,wednesdaytime4,wednesdaysubject5,wednesdaytime5,wednesdaysubject6,wednesdaytime6))
			elif wednesdayschedule==10:
				wednesdaysubject1=data["wednesdaysubject1"]
				wednesdaytime1=data["wednesdaytime1"]
				wednesdaysubject2=data["wednesdaysubject2"]
				wednesdaytime2=data["wednesdaytime2"]
				wednesdaysubject3=data["wednesdaysubject3"]
				wednesdaytime3=data["wednesdaytime3"]
				wednesdaysubject4=data["wednesdaysubject4"]
				wednesdaytime4=data["wednesdaytime4"]
				wednesdaysubject5=data["wednesdaysubject5"]
				wednesdaytime5=data["wednesdaytime5"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3,wednesdaysubject4,wednesdaytime4,wednesdaysubject5,wednesdaytime5))
			elif wednesdayschedule==8:
				wednesdaysubject1=data["wednesdaysubject1"]
				wednesdaytime1=data["wednesdaytime1"]
				wednesdaysubject2=data["wednesdaysubject2"]
				wednesdaytime2=data["wednesdaytime2"]
				wednesdaysubject3=data["wednesdaysubject3"]
				wednesdaytime3=data["wednesdaytime3"]
				wednesdaysubject4=data["wednesdaysubject4"]
				wednesdaytime4=data["wednesdaytime4"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3,wednesdaysubject4,wednesdaytime4))
			elif wednesdayschedule==6:
				wednesdaysubject1=data["wednesdaysubject1"]
				wednesdaytime1=data["wednesdaytime1"]
				wednesdaysubject2=data["wednesdaysubject2"]
				wednesdaytime2=data["wednesdaytime2"]
				wednesdaysubject3=data["wednesdaysubject3"]
				wednesdaytime3=data["wednesdaytime3"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3))
			elif wednesdayschedule==4:
				wednesdaysubject1=data["wednesdaysubject1"]
				wednesdaytime1=data["wednesdaytime1"]
				wednesdaysubject2=data["wednesdaysubject2"]
				wednesdaytime2=data["wednesdaytime2"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2))
			elif wednesdayschedule==2:
				wednesdaysubject1=data["wednesdaysubject1"]
				wednesdaytime1=data["wednesdaytime1"]
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(wednesdaysubject1,wednesdaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for wednesday or you forgot to input.")
		elif day=="thursday" or day== "thurs":
			if thursdayschedule==14:
				thursdaysubject1=data["thursdaysubject1"]
				thursdaytime1=data["thursdaytime1"]
				thursdaysubject2=data["thursdaysubject2"]
				thursdaytime2=data["thursdaytime2"]
				thursdaysubject3=data["thursdaysubject3"]
				thursdaytime3=data["thursdaytime3"]
				thursdaysubject4=data["thursdaysubject4"]
				thursdaytime4=data["thursdaytime4"]
				thursdaysubject5=data["thursdaysubject5"]
				thursdaytime5=data["thursdaytime5"]
				thursdaysubject6=data["thursdaysubject6"]
				thursdaytime6=data["thursdaytime6"]
				thursdaysubject7=data["thursdaysubject7"]
				thursdaytime7=data["thursdaytime7"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3,thursdaysubject4,thursdaytime4,thursdaysubject5,thursdaytime5,thursdaysubject6,thursdaytime6,thursdaysubject7,thursdaytime7))
			elif thursdayschedule==12:
				thursdaysubject1=data["thursdaysubject1"]
				thursdaytime1=data["thursdaytime1"]
				thursdaysubject2=data["thursdaysubject2"]
				thursdaytime2=data["thursdaytime2"]
				thursdaysubject3=data["thursdaysubject3"]
				thursdaytime3=data["thursdaytime3"]
				thursdaysubject4=data["thursdaysubject4"]
				thursdaytime4=data["thursdaytime4"]
				thursdaysubject5=data["thursdaysubject5"]
				thursdaytime5=data["thursdaytime5"]
				thursdaysubject6=data["thursdaysubject6"]
				thursdaytime6=data["thursdaytime6"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3,thursdaysubject4,thursdaytime4,thursdaysubject5,thursdaytime5,thursdaysubject6,thursdaytime6))
			elif thursdayschedule==10:
				thursdaysubject1=data["thursdaysubject1"]
				thursdaytime1=data["thursdaytime1"]
				thursdaysubject2=data["thursdaysubject2"]
				thursdaytime2=data["thursdaytime2"]
				thursdaysubject3=data["thursdaysubject3"]
				thursdaytime3=data["thursdaytime3"]
				thursdaysubject4=data["thursdaysubject4"]
				thursdaytime4=data["thursdaytime4"]
				thursdaysubject5=data["thursdaysubject5"]
				thursdaytime5=data["thursdaytime5"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3,thursdaysubject4,thursdaytime4,thursdaysubject5,thursdaytime5))
			elif thursdayschedule==8:
				thursdaysubject1=data["thursdaysubject1"]
				thursdaytime1=data["thursdaytime1"]
				thursdaysubject2=data["thursdaysubject2"]
				thursdaytime2=data["thursdaytime2"]
				thursdaysubject3=data["thursdaysubject3"]
				thursdaytime3=data["thursdaytime3"]
				thursdaysubject4=data["thursdaysubject4"]
				thursdaytime4=data["thursdaytime4"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3,thursdaysubject4,thursdaytime4))
			elif thursdayschedule==6:
				thursdaysubject1=data["thursdaysubject1"]
				thursdaytime1=data["thursdaytime1"]
				thursdaysubject2=data["thursdaysubject2"]
				thursdaytime2=data["thursdaytime2"]
				thursdaysubject3=data["thursdaysubject3"]
				thursdaytime3=data["thursdaytime3"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3))
			elif thursdayschedule==4:
				thursdaysubject1=data["thursdaysubject1"]
				thursdaytime1=data["thursdaytime1"]
				thursdaysubject2=data["thursdaysubject2"]
				thursdaytime2=data["thursdaytime2"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2))
			elif thursdayschedule==2:
				thursdaysubject1=data["thursdaysubject1"]
				thursdaytime1=data["thursdaytime1"]
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(thursdaysubject1,thursdaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for thursday or you forgot to input.")
		elif day=="friday" or day== "fri":
			if fridayschedule==14:
				fridaysubject1=data["fridaysubject1"]
				fridaytime1=data["fridaytime1"]
				fridaysubject2=data["fridaysubject2"]
				fridaytime2=data["fridaytime2"]
				fridaysubject3=data["fridaysubject3"]
				fridaytime3=data["fridaytime3"]
				fridaysubject4=data["fridaysubject4"]
				fridaytime4=data["fridaytime4"]
				fridaysubject5=data["fridaysubject5"]
				fridaytime5=data["fridaytime5"]
				fridaysubject6=data["fridaysubject6"]
				fridaytime6=data["fridaytime6"]
				fridaysubject7=data["fridaysubject7"]
				fridaytime7=data["fridaytime7"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3,fridaysubject4,fridaytime4,fridaysubject5,fridaytime5,fridaysubject6,fridaytime6,fridaysubject7,fridaytime7))
			elif fridayschedule==12:
				fridaysubject1=data["fridaysubject1"]
				fridaytime1=data["fridaytime1"]
				fridaysubject2=data["fridaysubject2"]
				fridaytime2=data["fridaytime2"]
				fridaysubject3=data["fridaysubject3"]
				fridaytime3=data["fridaytime3"]
				fridaysubject4=data["fridaysubject4"]
				fridaytime4=data["fridaytime4"]
				fridaysubject5=data["fridaysubject5"]
				fridaytime5=data["fridaytime5"]
				fridaysubject6=data["fridaysubject6"]
				fridaytime6=data["fridaytime6"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3,fridaysubject4,fridaytime4,fridaysubject5,fridaytime5,fridaysubject6,fridaytime6))
			elif fridayschedule==10:
				fridaysubject1=data["fridaysubject1"]
				fridaytime1=data["fridaytime1"]
				fridaysubject2=data["fridaysubject2"]
				fridaytime2=data["fridaytime2"]
				fridaysubject3=data["fridaysubject3"]
				fridaytime3=data["fridaytime3"]
				fridaysubject4=data["fridaysubject4"]
				fridaytime4=data["fridaytime4"]
				fridaysubject5=data["fridaysubject5"]
				fridaytime5=data["fridaytime5"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3,fridaysubject4,fridaytime4,fridaysubject5,fridaytime5))
			elif fridayschedule==8:
				fridaysubject1=data["fridaysubject1"]
				fridaytime1=data["fridaytime1"]
				fridaysubject2=data["fridaysubject2"]
				fridaytime2=data["fridaytime2"]
				fridaysubject3=data["fridaysubject3"]
				fridaytime3=data["fridaytime3"]
				fridaysubject4=data["fridaysubject4"]
				fridaytime4=data["fridaytime4"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3,fridaysubject4,fridaytime4))
			elif fridayschedule==6:
				fridaysubject1=data["fridaysubject1"]
				fridaytime1=data["fridaytime1"]
				fridaysubject2=data["fridaysubject2"]
				fridaytime2=data["fridaytime2"]
				fridaysubject3=data["fridaysubject3"]
				fridaytime3=data["fridaytime3"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3))
			elif fridayschedule==4:
				fridaysubject1=data["fridaysubject1"]
				fridaytime1=data["fridaytime1"]
				fridaysubject2=data["fridaysubject2"]
				fridaytime2=data["fridaytime2"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2))
			elif fridayschedule==2:
				fridaysubject1=data["fridaysubject1"]
				fridaytime1=data["fridaytime1"]
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(fridaysubject1,fridaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for friday or you forgot to input.")
		elif day=="saturday" or day== "sat":
			if saturdayschedule==14:
				saturdaysubject1=data["saturdaysubject1"]
				saturdaytime1=data["saturdaytime1"]
				saturdaysubject2=data["saturdaysubject2"]
				saturdaytime2=data["saturdaytime2"]
				saturdaysubject3=data["saturdaysubject3"]
				saturdaytime3=data["saturdaytime3"]
				saturdaysubject4=data["saturdaysubject4"]
				saturdaytime4=data["saturdaytime4"]
				saturdaysubject5=data["saturdaysubject5"]
				saturdaytime5=data["saturdaytime5"]
				saturdaysubject6=data["saturdaysubject6"]
				saturdaytime6=data["saturdaytime6"]
				saturdaysubject7=data["saturdaysubject7"]
				saturdaytime7=data["saturdaytime7"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3,saturdaysubject4,saturdaytime4,saturdaysubject5,saturdaytime5,saturdaysubject6,saturdaytime6,saturdaysubject7,saturdaytime7))
			elif saturdayschedule==12:
				saturdaysubject1=data["saturdaysubject1"]
				saturdaytime1=data["saturdaytime1"]
				saturdaysubject2=data["saturdaysubject2"]
				saturdaytime2=data["saturdaytime2"]
				saturdaysubject3=data["saturdaysubject3"]
				saturdaytime3=data["saturdaytime3"]
				saturdaysubject4=data["saturdaysubject4"]
				saturdaytime4=data["saturdaytime4"]
				saturdaysubject5=data["saturdaysubject5"]
				saturdaytime5=data["saturdaytime5"]
				saturdaysubject6=data["saturdaysubject6"]
				saturdaytime6=data["saturdaytime6"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3,saturdaysubject4,saturdaytime4,saturdaysubject5,saturdaytime5,saturdaysubject6,saturdaytime6))
			elif saturdayschedule==10:
				saturdaysubject1=data["saturdaysubject1"]
				saturdaytime1=data["saturdaytime1"]
				saturdaysubject2=data["saturdaysubject2"]
				saturdaytime2=data["saturdaytime2"]
				saturdaysubject3=data["saturdaysubject3"]
				saturdaytime3=data["saturdaytime3"]
				saturdaysubject4=data["saturdaysubject4"]
				saturdaytime4=data["saturdaytime4"]
				saturdaysubject5=data["saturdaysubject5"]
				saturdaytime5=data["saturdaytime5"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3,saturdaysubject4,saturdaytime4,saturdaysubject5,saturdaytime5))
			elif saturdayschedule==8:
				saturdaysubject1=data["saturdaysubject1"]
				saturdaytime1=data["saturdaytime1"]
				saturdaysubject2=data["saturdaysubject2"]
				saturdaytime2=data["saturdaytime2"]
				saturdaysubject3=data["saturdaysubject3"]
				saturdaytime3=data["saturdaytime3"]
				saturdaysubject4=data["saturdaysubject4"]
				saturdaytime4=data["saturdaytime4"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3,saturdaysubject4,saturdaytime4))
			elif saturdayschedule==6:
				saturdaysubject1=data["saturdaysubject1"]
				saturdaytime1=data["saturdaytime1"]
				saturdaysubject2=data["saturdaysubject2"]
				saturdaytime2=data["saturdaytime2"]
				saturdaysubject3=data["saturdaysubject3"]
				saturdaytime3=data["saturdaytime3"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3))
			elif saturdayschedule==4:
				saturdaysubject1=data["saturdaysubject1"]
				saturdaytime1=data["saturdaytime1"]
				saturdaysubject2=data["saturdaysubject2"]
				saturdaytime2=data["saturdaytime2"]
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2))
			elif saturdayschedule==2:
				saturdaysubject1=data["saturdaysubject1"]
				saturdaytime1=data["saturdaytime1"]
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(saturdaysubject1,saturdaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for saturday or you forgot to input.")
		else:
			await interaction.response.send_message("there's an oopsies that i probably forogt to code")

										


				
bot.run(TOKEN)

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

bot = commands.Bot(command_prefix="scriminfo", intents=intents, caseinsensitive=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
initialized = 0

@bot.event
async def on_ready():
    print("Commands loading...")
    await bot.tree.sync()
    print("Commands are ready.")

@bot.tree.command(name="resetschedule",description="reset or initialize schedule")
async def resetschedule(interaction:discord.Interaction):
	with open('schedule.json', 'w+') as file:
		initialize=json.load(file)
		initialize['mondaysubject1']="0"
		initialize['mondaytime1']=0
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
		initialize['tuesdaysubject1']="0"
		initialize['tuesdaytime1']=0
		initialize['tuesdaysubject2']="0"
		initialize['tuesdaytime2']=0
		initialize['tuesdaysubject3']="0"
		initialize['tuesdaytime3']=0
		initialize['tuesdaysubject4']="0"
		initialize['tuesdaytime4']=0
		initialize['tuesdaysubject5']="0"
		initialize['tuesdaytime5']=0
		initialize['tuesdaysubject6']="0"
		initialize['tuesdaytime6']=0
		initialize['tuesdaysubject7']="0"
		initialize['tuesdaytime7']=0
		initialize['wednesdaysubject1']="0"
		initialize['wednesdaytime1']=0
		initialize['wednesdaysubject2']="0"
		initialize['wednesdaytime2']=0
		initialize['wednesdaysubject3']="0"
		initialize['wednesdaytime3']=0
		initialize['wednesdaysubject4']="0"
		initialize['wednesdaytime4']=0
		initialize['wednesdaysubject5']="0"
		initialize['wednesdaytime5']=0
		initialize['wednesdaysubject6']="0"
		initialize['wednesdaytime6']=0
		initialize['wednesdaysubject7']="0"
		initialize['wednesdaytime7']=0
		initialize['thursdaysubject1']="0"
		initialize['thursdaytime1']=0
		initialize['thursdaysubject2']="0"
		initialize['thursdaytime2']=0
		initialize['thursdaysubject3']="0"
		initialize['thursdaytime3']=0
		initialize['thursdaysubject4']="0"
		initialize['thursdaytime4']=0
		initialize['thursdaysubject5']="0"
		initialize['thursdaytime5']=0
		initialize['thursdaysubject6']="0"
		initialize['thursdaytime6']=0
		initialize['thursdaysubject7']="0"
		initialize['thursdaytime7']=0
		initialize['fridaysubject1']="0"
		initialize['fridaytime1']=0
		initialize['fridaysubject2']="0"
		initialize['fridaytime2']=0
		initialize['fridaysubject3']="0"
		initialize['fridaytime3']=0
		initialize['fridaysubject4']="0"
		initialize['fridaytime4']=0
		initialize['fridaysubject5']="0"
		initialize['fridaytime5']=0
		initialize['fridaysubject6']="0"
		initialize['fridaytime6']=0
		initialize['fridaysubject7']="0"
		initialize['fridaytime7']=0
		initialize['saturdaysubject1']="0"
		initialize['saturdaytime1']=0
		initialize['saturdaysubject2']="0"
		initialize['saturdaytime2']=0
		initialize['saturdaysubject3']="0"
		initialize['saturdaytime3']=0
		initialize['saturdaysubject4']="0"
		initialize['saturdaytime4']=0
		initialize['saturdaysubject5']="0"
		initialize['saturdaytime5']=0
		initialize['saturdaysubject6']="0"
		initialize['saturdaytime6']=0
		initialize['saturdaysubject7']="0"
		initialize['saturdaytime7']=0
		json.dump(initialize,file)
	await interaction.response.send_message("initialized.")


@bot.tree.command(name="inputschedule", description="input schedule")
async def inputsched(interaction:discord.Interaction, subject:str, day: str, time:int):
	if day=="monday" or "mon":
		with open('schedule.json', 'r+') as file:
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
		if "mondaytime1" ==0:
			data['mondaysubject1']=subject
			data['mondaytime1']=time
			with open('schedule.json', 'w') as file:
				json.dump(data, file)
				await interaction.response.send_message("inputted")
		elif "mondaysubject1" !=0:
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
			await interaction.response.send_message("please check input again")
	elif day=="tuesday" or "tues":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
		if "tuesdaytime1" ==0:
			data['tuesdaysubject1']=subject
			data['tuesdaytime1']=time
			with open('schedule.json', 'w') as file:
				json.dump(data, file)
				await interaction.response.send_message("inputted")
		elif "tuesdaysubject1" !=0:
			data['tuesdaysubject2']=subject
			data['tuesdaytime2']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "tuesdaysubject2" !=0:
			data['tuesdaysubject3']=subject
			data['tuesdaytime3']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "tuesdaysubject3" !=0:
			data['tuesdaysubject4']=subject
			data['tuesdaytime4']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "tuesdaysubject4" !=0:
			data['tuesdaysubject5']=subject
			data['tuesdaytime5']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "tuesdaysubject5" !=0:
			data['tuesdaysubject6']=subject
			data['tuesdaytime6']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "tuesdaysubject6" !=0:
			data['tuesdaysubject7']=subject
			data['tuesdaytime7']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "tuesdaysubject7" !=0:
			await interaction.response.send_message("you can only put 7 subjects maximum.")
		else:
			await interaction.response.send_message("please check input again")
	if day=="wednesday" or "wed":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
		if "wednesdaytime1" ==0:
			data['wednesdaysubject1']=subject
			data['wednesdaytime1']=time
			with open('schedule.json', 'w') as file:
				json.dump(data, file)
				await interaction.response.send_message("inputted")
		elif "wednesdaysubject1" !=0:
			data['wednesdaysubject2']=subject
			data['wednesdaytime2']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "wednesdaysubject2" !=0:
			data['wednesdaysubject3']=subject
			data['wednesdaytime3']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "wednesdaysubject3" !=0:
			data['wednesdaysubject4']=subject
			data['wednesdaytime4']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "wednesdaysubject4" !=0:
			data['wednesdaysubject5']=subject
			data['wednesdaytime5']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "wednesdaysubject5" !=0:
			data['wednesdaysubject6']=subject
			data['wednesdaytime6']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "wednesdaysubject6" !=0:
			data['wednesdaysubject7']=subject
			data['wednesdaytime7']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "wednesdaysubject7" !=0:
			await interaction.response.send_message("you can only put 7 subjects maximum.")
		else:
			await interaction.response.send_message("please check input again")
	if day=="thursday" or "thurs":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
		if "thursdaytime1" ==0:
			data['thursdaysubject1']=subject
			data['thursdaytime1']=time
			with open('schedule.json', 'w') as file:
				json.dump(data, file)
				await interaction.response.send_message("inputted")
		elif "thursdaysubject1" !=0:
			data['thursdaysubject2']=subject
			data['thursdaytime2']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "thursdaysubject2" !=0:
			data['thursdaysubject3']=subject
			data['thursdaytime3']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "thursdaysubject3" !=0:
			data['thursdaysubject4']=subject
			data['thursdaytime4']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "thursdaysubject4" !=0:
			data['thursdaysubject5']=subject
			data['thursdaytime5']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "thursdaysubject5" !=0:
			data['thursdaysubject6']=subject
			data['thursdaytime6']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "thursdaysubject6" !=0:
			data['thursdaysubject7']=subject
			data['thursdaytime7']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "thursdaysubject7" !=0:
			await interaction.response.send_message("you can only put 7 subjects maximum.")
		else:
			await interaction.response.send_message("please check input again")
	if day=="friday" or "fri":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
		if "fridaytime1" ==0:
			data['fridaysubject1']=subject
			data['fridaytime1']=time
			with open('schedule.json', 'w') as file:
				json.dump(data, file)
				await interaction.response.send_message("inputted")
		elif "fridaysubject1" !=0:
			data['fridaysubject2']=subject
			data['fridaytime2']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "fridaysubject2" !=0:
			data['fridaysubject3']=subject
			data['fridaytime3']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "fridaysubject3" !=0:
			data['fridaysubject4']=subject
			data['fridaytime4']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "fridaysubject4" !=0:
			data['fridaysubject5']=subject
			data['fridaytime5']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "fridaysubject5" !=0:
			data['fridaysubject6']=subject
			data['fridaytime6']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "fridaysubject6" !=0:
			data['fridaysubject7']=subject
			data['fridaytime7']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "fridaysubject7" !=0:
			await interaction.response.send_message("you can only put 7 subjects maximum.")
		else:
			await interaction.response.send_message("please check input again")
	if day=="saturday" or "sat":
		with open('schedule.json', 'r+') as file:
			data=json.load(file)
		if "saturdaytime1" ==0:
			data['saturdaysubject1']=subject
			data['saturdaytime1']=time
			with open('schedule.json', 'w') as file:
				json.dump(data, file)
				await interaction.response.send_message("inputted")
		elif "saturdaysubject1" !=0:
			data['saturdaysubject2']=subject
			data['saturdaytime2']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "saturdaysubject2" !=0:
			data['saturdaysubject3']=subject
			data['saturdaytime3']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "saturdaysubject3" !=0:
			data['saturdaysubject4']=subject
			data['saturdaytime4']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "saturdaysubject4" !=0:
			data['saturdaysubject5']=subject
			data['saturdaytime5']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "saturdaysubject5" !=0:
			data['saturdaysubject6']=subject
			data['saturdaytime6']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "saturdaysubject6" !=0:
			data['saturdaysubject7']=subject
			data['saturdaytime7']=time
			with open('schedule.json','w') as file:
				json.dump(data,file)
				await interaction.response.send_message("inputted")
		elif "saturdaysubject7" !=0:
			await interaction.response.send_message("you can only put 7 subjects maximum.")
		else:
			await interaction.response.send_message("please check input again")
	else:
		await interaction.response.send_message("error, please try again.")

@bot.tree.command(name="getschedule", description="get schedule")
async def getschedule(interaction:discord.Interaction, day:str):
	with open('schedule.json','r+') as file:
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
		if day=="monday" or "mon":
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
		elif day=="tuesday" or "tues":
			if "tuesdaysubject7" in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3,tuesdaysubject4,tuesdaytime4,tuesdaysubject5,tuesdaytime5,tuesdaysubject6,tuesdaytime6,tuesdaysubject7,tuesdaytime7))
			elif "tuesdaysubject7" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3,tuesdaysubject4,tuesdaytime4,tuesdaysubject5,tuesdaytime5,tuesdaysubject6,tuesdaytime6))
			elif "tuesdaysubject6" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3,tuesdaysubject4,tuesdaytime4,tuesdaysubject5,tuesdaytime5))
			elif "tuesdaysubject5" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3,tuesdaysubject4,tuesdaytime4))
			elif "tuesdaysubject4" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2,tuesdaysubject3,tuesdaytime3))
			elif "tuesdaysubject3" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(tuesdaysubject1,tuesdaytime1,tuesdaysubject2,tuesdaytime2))
			elif "tuesdaysubject2" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(tuesdaysubject1,tuesdaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for tuesday or you forgot to input.")
		elif day=="wednesday" or "wed":
			if "wednesdaysubject7" in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3,wednesdaysubject4,wednesdaytime4,wednesdaysubject5,wednesdaytime5,wednesdaysubject6,wednesdaytime6,wednesdaysubject7,wednesdaytime7))
			elif "wednesdaysubject7" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3,wednesdaysubject4,wednesdaytime4,wednesdaysubject5,wednesdaytime5,wednesdaysubject6,wednesdaytime6))
			elif "wednesdaysubject6" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3,wednesdaysubject4,wednesdaytime4,wednesdaysubject5,wednesdaytime5))
			elif "wednesdaysubject5" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3,wednesdaysubject4,wednesdaytime4))
			elif "wednesdaysubject4" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2,wednesdaysubject3,wednesdaytime3))
			elif "wednesdaysubject3" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(wednesdaysubject1,wednesdaytime1,wednesdaysubject2,wednesdaytime2))
			elif "wednesdaysubject2" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(wednesdaysubject1,wednesdaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for wednesday or you forgot to input.")
		elif day=="thursday" or "thurs":
			if "thursdaysubject7" in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3,thursdaysubject4,thursdaytime4,thursdaysubject5,thursdaytime5,thursdaysubject6,thursdaytime6,thursdaysubject7,thursdaytime7))
			elif "thursdaysubject7" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3,thursdaysubject4,thursdaytime4,thursdaysubject5,thursdaytime5,thursdaysubject6,thursdaytime6))
			elif "thursdaysubject6" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3,thursdaysubject4,thursdaytime4,thursdaysubject5,thursdaytime5))
			elif "thursdaysubject5" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3,thursdaysubject4,thursdaytime4))
			elif "thursdaysubject4" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2,thursdaysubject3,thursdaytime3))
			elif "thursdaysubject3" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(thursdaysubject1,thursdaytime1,thursdaysubject2,thursdaytime2))
			elif "thursdaysubject2" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(thursdaysubject1,thursdaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for thursday or you forgot to input.")
		elif day=="friday" or "fri":
			if "fridaysubject7" in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3,fridaysubject4,fridaytime4,fridaysubject5,fridaytime5,fridaysubject6,fridaytime6,fridaysubject7,fridaytime7))
			elif "fridaysubject7" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3,fridaysubject4,fridaytime4,fridaysubject5,fridaytime5,fridaysubject6,fridaytime6))
			elif "fridaysubject6" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3,fridaysubject4,fridaytime4,fridaysubject5,fridaytime5))
			elif "fridaysubject5" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3,fridaysubject4,fridaytime4))
			elif "fridaysubject4" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2,fridaysubject3,fridaytime3))
			elif "fridaysubject3" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(fridaysubject1,fridaytime1,fridaysubject2,fridaytime2))
			elif "fridaysubject2" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(fridaysubject1,fridaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for friday or you forgot to input.")
		elif day=="saturday" or "sat":
			if "saturdaysubject7" in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3,saturdaysubject4,saturdaytime4,saturdaysubject5,saturdaytime5,saturdaysubject6,saturdaytime6,saturdaysubject7,saturdaytime7))
			elif "saturdaysubject7" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3,saturdaysubject4,saturdaytime4,saturdaysubject5,saturdaytime5,saturdaysubject6,saturdaytime6))
			elif "saturdaysubject6" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3,saturdaysubject4,saturdaytime4,saturdaysubject5,saturdaytime5))
			elif "saturdaysubject5" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3,saturdaysubject4,saturdaytime4))
			elif "saturdaysubject4" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2,saturdaysubject3,saturdaytime3))
			elif "saturdaysubject3" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}, and {} at {}." .format(saturdaysubject1,saturdaytime1,saturdaysubject2,saturdaytime2))
			elif "saturdaysubject2" not in file:
				await interaction.response.send_message("Your schedule for today is: {} at {}." .format(saturdaysubject1,saturdaytime1))
			else:
				await interaction.response.send_message("You either don't have a schedule for saturday or you forgot to input.")
		else:
			await interaction.response.send_message("please input a valid day.")

bot.run(TOKEN)
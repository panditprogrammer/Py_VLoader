import youtube_dl
import os
ydl_opts ={}
def download():
	print("\n Please wait \n downloading...")
	try:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([link_video])
			print("\n  Successfully Downloaded \n ")
	except:
		print("Unable to download may be link is not valid or something else\n")

		
cp= 1
while(cp):
	os.system('cls')
	print(" \t ******* YouTube Video Downloader  : PanditProgrammer.com ******* \n \n ")
	print("Note :- Location of downloaded Video is current \n \t directory where Downloader is running.  ")
	print("\t Paste Your Desire YouTube Video Link and wait until download\n  ")
	link_video = input(" Enter Link Of The Video  \n ")
	download()
	print("  Do you want to download another one? \n  Enter any Key to Continue \n  Else Press Enter key to Exit")
	cp =input ("  ")
	
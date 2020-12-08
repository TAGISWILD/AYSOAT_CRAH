import itertools
from array import array
import string
import sys
import argparse


print("""


       __     _______  ____       _______    _____ _____            _    _ 
     /\\ \   / / ____|/ __ \   /\|__   __|  / ____|  __ \     /\   | |  | |
    /  \\ \_/ / (___ | |  | | /  \  | |    | |    | |__) |   /  \  | |__| |
   / /\ \\   / \___ \| |  | |/ /\ \ | |    | |    |  _  /   / /\ \ |  __  |
  / ____ \| |  ____) | |__| / ____ \| |   | |____| | \ \  / ____ \| |  | |
 /_/    \_\_| |_____/ \____/_/    \_\_|    \_____|_|  \_\/_/    \_\_|  |_|
                                                                           
                                                                           

       Made By Atharva Chauhan For AYSOAT Ltd.                                                                    
                                                                           


""")

def main():
	try:
		parser = argparse.ArgumentParser(prog="sniper-h.py", add_help=True, usage=(
		"python mkls.py [-W characters_numbers_symbols] [-M mattresses] [-O save\show outpot]"))
		parser.add_argument("-W", dest="characters_numbers_symbols", required=True, help=": [-CNS] characters/numbers/symbols values")
		parser.add_argument("-M", dest="mattresses", required=True, help=": [-W] path word list")
		parser.add_argument("-O", dest="output_save_show", required=True, help=": [-O] save/show outpot",
		choices=["save","show"])
		args = parser.parse_args()
		def order():
			
			if args.output_save_show == "save" :
				output = open("wordlist.txt", "w")
				sys.stdout = output
				for wl in itertools.product(args.characters_numbers_symbols, repeat=int(args.mattresses)):
					try:
						op = ''.join(wl)
					except AttributeError:
						op = string.join(wl, '')
					print(op)
				output.close

			elif args.output_save_show == "show" :
				for wl in itertools.product(args.characters_numbers_symbols, repeat=int(args.mattresses)):
					try:
						op = ''.join(wl)
					except AttributeError:
						op = string.join(wl, '')
					print(op)
			else:
				print("[ERROR] Not found!")
		order()

	except ValueError:
		print("\n\n[ERROR] You must enter just numbers !.")
	except KeyboardInterrupt:
		pass
if __name__ == "__main__" :
	main()


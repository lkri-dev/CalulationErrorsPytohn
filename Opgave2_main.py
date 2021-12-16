"""
Tips
Press Shift+F10 to execute it or replace it with your code.
Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Dette program er lavet til at øve fejlfinding i kode.
Her er et program som skal udregne Ohm lov, et af reasultaterne er forkerte. Hvorfor?
"""
import os

def ohms_lov(r_ohms = None, i_amp = None, u_volt = None):
	if r_ohms and i_amp is not None:
		u_volt = i_amp * r_ohms
		return u_volt
	if r_ohms and u_volt is not None:
		i_amp = u_volt / r_ohms
		return i_amp
	if u_volt and i_amp is not None:
		r_ohms = u_volt * i_amp
		return r_ohms
	else:
		return 0

if __name__ == '__main__':
	loop_control = True
	liste = ['Udregn R', 'Udregn I', 'Udregn U', 'Afslut']
	while(loop_control):
		count = 1
		for mulighed in liste:
			print('{tal}: {mulighed}'.format(tal=liste.index(mulighed), mulighed=mulighed))
			count = count + 1

		valg = input('Vælg hvilken en af varialberne du vil udregne og intasts dens nummer:')

		if valg == '0':
			print('{valg} bliv valgt'.format(valg=liste[0]))
			print(ohms_lov(
				i_amp=float(input('Indtast I')),
				u_volt=float(input('Indtast U'))))
		elif valg == '1':
			print('{valg} bliv valgt'.format(valg=liste[1]))
			print(ohms_lov(
				r_ohms=float(input('Indtast R')),
				u_volt=float(input('Indtast U'))))
		elif valg == '2':
			print('{valg} bliv valgt'.format(valg=liste[2]))
			print(ohms_lov(
				i_amp=float(input('Indtast I')),
				r_ohms=float(input('Indtast R'))))
		elif valg == '3':
			print('{valg} bliv valgt'.format(valg=liste[3]))
			loop_control = False
		else:
			print('Ingen af mulighederne blev valgt, prøv igen')
		input()
		os.system('cls')



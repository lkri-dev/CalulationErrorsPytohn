"""
Tips
Press Shift+F10 to execute it or replace it with your code.
Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Dette program er lavet til at øve fejlfinding i kode.
Her er et program som skal udregne BMI baseret på en vægt i kg og en højde i m, det giver er forkert resultat. Hvorfor?
"""

def bmi_udregner(vaegt, hoejde):
    return (hoejde * hoejde) / vaegt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    kg = float(input('Indtast en vægt i kg'))
    m = float(input('Indtast en højde i m'))
    print(bmi_udregner(kg, m))

#Program przyjmuje dwie liczby zadane przez użytkownika i wykonuje na nich zlecone działanie

import logging
logging.basicConfig(
    filename='log.txt',                                     #nazwa pliku logów
    level=logging.INFO,                                     #poziom logowania
    format='%(asctime)s - %(message)s')                     #format logów


def kalkulator(dzialanie, liczby):
#Funkcja wykonuje zadane działanie na podanych liczbach
#Argumenty: dzialanie - int z zakresu [1,4]
#           liczby - lista floatów
    if dzialanie == 1:
        wynik = sum(liczby)
    elif dzialanie == 2:
        wynik = liczby[0] - liczby[1]
    elif dzialanie == 3:
        wynik = 1
        for liczba in liczby:
            wynik *= liczba
    elif dzialanie == 4:
        wynik = liczby[0] / liczby[1]
    else:
        exit(1)
    return wynik

def sprawdz_dzialanie(dzialanie):
#Funkcja sprawdza, czy wprowadzono poprawną wartość zmiennej "dzialanie" i zwraca wartość boolean
#Argumenty: dzialanie - dowolny string
    dopuszczalne_dzialania = ('0', '1', '2', '3', '4')
    if dzialanie in dopuszczalne_dzialania:
        return True
    else:
        return False
    
def co_robie(dzialanie, liczby):
#Funkcja przygotowuje tekst opisujący wykonywane działanie i jego składniki
#Argumenty: dzialanie - int z zakresu [1,4]
#           liczby - lista dowolnych wartości (konwertowane na stringi)
        dict_dzialan = {
            1: ("Dodaję ", " i "), 
            2: ("Od ", " odejmuję "), 
            3: ("Mnożę ", " i "), 
            4: ("Dzielę ", " przez ")}
        
        result = dict_dzialan[dzialanie][0]
        for liczba in liczby[:-1]:
            result = result + str(liczba) + dict_dzialan[dzialanie][1]
        result = result + str(liczby[-1])

        return result
        

#Część wykonywalna
if __name__ == "__main__":
    logging.info("Uruchomienie skryptu")

    #Ustalenie rodzaju działania matematycznego
    text_promptu = "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, 0 Zamknij: "  
    dzialanie = ""
    
    while sprawdz_dzialanie(dzialanie) == False:            #dopóki nie wpisano poprawnej liczby
        dzialanie = input(text_promptu)                     #wpisz numer działania
        if sprawdz_dzialanie(dzialanie) == False:           #jeżeli błędne wprowadzenie
            print("Błąd: Wprowadź poprawną liczbę.")
        elif dzialanie == '0':                              #obsługa przypadku wyjścia
            print("Kończę pracę")
            logging.info("Zakończenie skryptu bez dokonywania obliczeń")
            exit(0)
        else:
            dzialanie = int(dzialanie)                      #jeżeli dzialanie poprawne, zmień na intergera i proceduj
            break
    
    
    #Wpisanie składników działania
    liczby = []
    
    if dzialanie in (2,4):                              #ustal ile max. może być składników działania
        limit_skladnikow = 2
    else:
        limit_skladnikow = 10
    
    while len(liczby) < limit_skladnikow:
        if len(liczby) < 2:
            skladnik = input(f"Podaj składnik {len(liczby)+1}: ")
        else:                                           #rozszerz tekst promptu dopiero od 3. składnika
            skladnik = input(f"Podaj składnik {len(liczby)+1} lub pozostaw puste, aby zakończyć wprowadzanie: ")             
            if skladnik == "":                          #jeżeli nic nie wpisano
                break                                   #przerwij pętlę while
        
        #obsługa błędnych danych wejściowych
        try:
            #zamień przecinek na kropkę i konwertuj na float
            liczby.append(float(skladnik.replace(',', '.')))
        except ValueError:
            print("Błąd: Wprowadź poprawną liczbę.")

        #obsługa dzielenia przez zero
        if dzialanie==4 and len(liczby)==2 and liczby[1]==0:
            del liczby[1]
            print("Nie próbuj dzielić przez zero: Wprowadź poprawną liczbę.")
            logging.info("Próba dzielenia przez zero")
        
    
    #wyświetl wynik
    logging.info(f"Przyjęto do działania {dzialanie} argumenty {liczby}")
    print(co_robie(dzialanie, liczby))
    wynik = kalkulator(dzialanie, liczby)
    logging.info(f"Wykonano działania z wynikiem {wynik}")
    print(f"Wynik to: {wynik}")    
    logging.info("Zakończenie skryptu")

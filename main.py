import json
from faker import Faker
import argparse

def generate_data(records):
    # Inizializza Faker
    fake = Faker()
    
    # Crea una lista per contenere tutti i dati
    data_list = []
    
    # Genera i dati fittizi
    for _ in range(records):
        data_list.append({
            'name': fake.name(),
            'address': fake.address(),
            'phone_number': fake.phone_number(),
            'email': fake.email()
            # Aggiungi altri campi qui se necessario
        })
    
    return data_list

def main():
    # Configura l'analisi degli argomenti
    parser = argparse.ArgumentParser(description="Generate fake JSON data.")
    parser.add_argument('records', type=int, help='Number of records to generate')

    # Estrai i valori degli argomenti
    args = parser.parse_args()

    # Genera i dati
    fake_data = generate_data(args.records)

    # Stampa i dati generati
    print(json.dumps(fake_data, indent=4))

if __name__ == "__main__":
    main()

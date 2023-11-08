#!/bin/bash

# Definire il nome dell'ambiente virtuale
VENV_NAME="json_test_factory_env"

# Creare l'ambiente virtuale
python3 -m venv $VENV_NAME

# Attivare l'ambiente virtuale
source $VENV_NAME/bin/activate

# Aggiornare pip all'ultima versione
pip install --upgrade pip

# Installare le dipendenze
pip install -r requirements.txt

echo "Ambiente virtuale creato e attivato. Per attivarlo manualmente usa 'source $VENV_NAME/bin/activate'."

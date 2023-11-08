# JSONtestFactory

## Introduzione
`JSONtestFactory` è uno script Python progettato per generare grandi volumi di dati JSON falsi ma strutturalmente verosimili, ideali per simulare dati sensibili durante i test di software e sistemi che richiedono input in formato JSON. Questo strumento è particolarmente utile per sviluppatori e tester che necessitano di un metodo sicuro e affidabile per testare le funzionalità senza il rischio di esporre dati reali.

## Scopo del Progetto
L'obiettivo principale di `JSONtestFactory` è fornire una soluzione rapida e personalizzabile per la creazione di dati di test. Utilizzando la libreria [Faker](https://faker.readthedocs.io/en/master/), questo script è in grado di produrre dati randomici che includono, ma non si limitano a, nomi, indirizzi, numeri di telefono e testi fittizi. Questi dati possono essere utilizzati per popolare database di test, per testare API, per la verifica della validazione dei dati e in molte altre situazioni di testing dove i dati reali non possono o non devono essere utilizzati.

## Caratteristiche
- **Generazione di dati falsi**: Crea dati realistici ma completamente fittizi.
- **Facilità d'uso**: Con pochi semplici passaggi, genera migliaia di record.
- **Scalabilità**: Adatto sia per piccoli test che per simulazioni di grandi dataset.
- **Personalizzazione della struttura dei dati**: Struttura i dati JSON in base alle esigenze specifiche del test. **[TODO]**

## Come Iniziare
Per iniziare a utilizzare `JSONtestFactory`, segui i passaggi di installazione qui sotto e personalizza lo script in base alle tue necessità.

## Installazione

Per installare e configurare l'ambiente virtuale necessario per eseguire `JSONtestFactory`, eseguire lo script `setup.sh`:

\```bash
./setup.sh
\```

## Esempi di Utilizzo

Dopo aver configurato l'ambiente come descritto nella sezione Installazione, puoi generare dati JSON fittizi eseguendo `main.py` con un argomento che specifica il numero di record da generare.

### Generare 10 record

Per generare un file JSON contenente 10 record fittizi:

\```bash
python main.py 10
\```

Questo comando stampa i dati JSON direttamente nella console. Se desideri salvare l'output in un file, puoi reindirizzare l'output in questo modo:

\```bash
python main.py 10 > output.json
\```

### Generare un Numero Maggiore di Record

Puoi anche generare un numero maggiore di record, come mostrato nell'esempio seguente per 1000 record:

\```bash
python main.py 1000 > output.json
\```

Assicurati di avere abbastanza memoria e spazio su disco se pianifichi di generare un numero molto grande di record.

## Licenza

`JSONtestFactory` è rilasciato sotto la licenza GNU General Public License v3.0, che è una licenza pubblica molto permissiva che consente la distribuzione, la modifica, e l'uso personale e commerciale del codice sorgente, a condizione che lo stesso diritto sia conservato nel software distribuito che include parti del `JSONtestFactory`.

Per maggiori dettagli sulla licenza, si prega di leggere il file `LICENSE` incluso in questa repository, o visitare [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

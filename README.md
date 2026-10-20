# Technologie Mowy — Grupa 6

Repozytorium grupowe do realizacji laboratoriów i projektu
z przedmiotu Technologie Mowy.

## Struktura

- `Laby/` — zadania laboratoryjne, osobny katalog dla każdego laboratorium.
  -  `data/` — dane źródłowe.
  -  `output/` - dane wyjściowe (wyłącznie lokalne). 
- `Projekt/` — projekt grupowy.
- `utils/` — wspólne narzędzia.
- `requirements.txt` — zależności Python.
- `pyproject.toml` — konfiguracja pakietu python.

## Środowisko

Utworzenie środowiska wirtualnego
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instalacja wymaganych bibliotek:

```bash
pip install -r requirements.txt
```

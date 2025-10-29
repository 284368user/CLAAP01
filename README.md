# Analiza Struktury PEB w Systemie Windows

Dokumentacja dotycząca struktury **PEB (Process Environment Block)** w systemie Windows, wykorzystywanej w debugowaniu, analizie złośliwego oprogramowania oraz monitorowaniu procesów.

![PEB Image](./source/media/image1.png)

## Budowanie dokumentacji

### Instalacja zależności

```bash
pip install -r requirements.txt
```

### Budowanie HTML

**Linux/macOS:**
```bash
make html
```

**Windows:**
```cmd
make.bat html
```

Wygenerowana dokumentacja będzie dostępna w katalogu `_build/html/`.

### Inne formaty

```bash
make latexpdf  # PDF przez LaTeX
make epub      # EPUB
make clean     # Czyszczenie plików budowy
```

## Optymalizacje wydajności

Ten projekt został zoptymalizowany pod kątem szybkości budowania. Zobacz [PERFORMANCE.md](PERFORMANCE.md) dla szczegółów.


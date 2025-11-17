# Pitch2Score

**Pitch2Score** es una aplicación en Python que permite:

- Afinar instrumentos en tiempo real
- Grabar pistas tipo loop
- Transcribir audio a partitura
- Exportar partituras a MusicXML, MIDI o PNG
- Transportar pistas a diferentes tonalidades
- Reproducir pistas en tiempo real usando audio o MIDI

## Tecnologías utilizadas

- Python 3.11+
- PyQt6 (interfaz gráfica)
- Librosa y Aubio (procesamiento de audio)
- Music21 (creación y exportación de partituras)
- Numpy y Pydub (manejo de audio)

## Estructura del proyecto

Pitch2Score/
├── gui/
│   ├── __init__.py
│   ├── main.py          # archivo principal para ejecutar la ventana
│   └── window.py        # definición de la ventana principal y widgets
│
├── audio/
│   ├── __init__.py
│   ├── tuner.py         # afinador en tiempo real
│   ├── recorder.py      # grabación de pistas
│   ├── looper.py        # reproducción tipo pedal loop
│   └── processing.py    # transcripción a notas y análisis de audio
│
├── notation/
│   ├── __init__.py
│   ├── builder.py       # construcción de partituras con music21
│   └── exporter.py      # exportación a MusicXML, MIDI, PNG
│
├── tests/               # opcional pero profesional: pruebas unitarias
│   ├── __init__.py
│   └── test_audio.py
│
├── README.md
├── .gitignore
└── LICENSE

"""Input interfaces.

This module provides input interfaces for common symbolic music formats,
MusPy's native JSON and YAML formats, other symbolic music libraries and
commonly-used representations in music generation.

Functions
---------

- from_event_representation
- from_mido
- from_music21
- from_music21_opus
- from_note_representation
- from_object
- from_pianoroll_representation
- from_pitch_representation
- from_pretty_midi
- from_pypianoroll
- from_representation
- load
- load_json
- load_yaml
- read
- read_abc
- read_abc_string
- read_midi
- read_musicxml

Errors
------

- MIDIError
- MusicXMLError

"""
from .abc import read_abc, read_abc_string
from .event import from_event_representation
from .json import load_json
from .midi import from_mido, from_pretty_midi, read_midi, MIDIError
from .music21 import from_music21, from_music21_opus
from .musicxml import read_musicxml, MusicXMLError
from .note import from_note_representation
from .pianoroll import from_pianoroll_representation, from_pypianoroll
from .pitch import from_pitch_representation
from .wrappers import from_object, from_representation, load, read
from .yaml import load_yaml

__all__ = [
    "MIDIError",
    "MusicXMLError",
    "from_event_representation",
    "from_mido",
    "from_music21",
    "from_music21_opus",
    "from_note_representation",
    "from_object",
    "from_pianoroll_representation",
    "from_pitch_representation",
    "from_pretty_midi",
    "from_pypianoroll",
    "from_representation",
    "load",
    "load_json",
    "load_yaml",
    "read",
    "read_abc",
    "read_abc_string",
    "read_midi",
    "read_musicxml",
]

# aktuell
_a personal assistant_


A robust NLU parser that generalizes well to OOV elements and successfully handles core intents.

A regression harness is used to assess coverage.

To update the NLU module run the following command from the `nlu` directory:

```$ python -m rasa_nlu.train --config config.yml --data data/data.md --fixed_model_name model20190119```

Use `console.py` to parse queries:

```$ python console.py model20190119 "recommend garage rock from 1991"```

Use `pytest` to assess parser coverage.


# Annotation Guidelines

Supported entity types:

  MOD
  WHO
  WORK
  ARTIST
  LABEL
  (REGION)
  (PLACE)
  TIME
  FORMAT
  RELEASE
  GENRE
  TEMP_SIG
  LAB_SIG
  PLAYLIST

Supported look ups:

  GENRE
  FORMAT
  RELEASE

Supported intents:

  SHARE
  REMEMBER
  RECOMMEND
  PLAYLIST
  SEARCH
  PLAY
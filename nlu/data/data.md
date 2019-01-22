<!--- 

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

--> 


## intent:share

- share [new](mod) [Broncho](artist) [album](release) with [Paul](who)
- show [Hadley](who) [eye in the sky](work) by [alan parsons project](artist)
- tell [george](who) about [abba](artist)
- share [u2](artist) with [frank](who) and [homer](who)
- let [bill](who) know about [madonna](artist)
- share [Band on the run](work) with (samantha)[who]
- share all [sleep](artist) releases [before](temp_sig) [1997](time) with [wayne](who)


## intent:remember

- remind me to check out the new [Gary War](artist) [album](release) [New Raytheonport](work)
- Remember [Misfits](artist) [song](release) [Hybird Moments](work)
- remember [Innuendo](work) by [queen](artist)
- remind me to listen to [brass buttons](work) by [gram parsons](artist)
- remember [album](release) [the pleasure principle](work)


## intent:recommend

- notable [garage rock](genre) [albums](release) released [in](temp_sig) [2011](time)
- recommend [1995](time) [grindcore](genre) releases
- recommend [beatles](artist) [after](temp_sig) [1971](time)
- good [Thelonious Monk](artist) releases
- good [jazz](genre)
- what is the best [Beethoven](artist) [song](release)


## intent:playlist

- add [Middle Child](work) by [Daniel Romano](artist) to playlist [normaltown](playlist)


## intent:search

- show me [Madeline](artist) [CDs](format) released [on](lab_sig) [Plan-it-X](label)
- Show me [John Maus](artist) releases [on](lab_sig) [Upset! The Rhythm](label)
- search all [Rameau](artist) releases [between](temp_sig) [1740](time) and [1750](time)
- all songs by [devo](artist)


## intent:play

- play [Judy Garland](artist) now

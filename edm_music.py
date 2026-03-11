from pyo import *
import random

# start audio server
s = Server().boot()
s.start()

# tempo EDM
BPM = 128
beat = 60.0 / BPM

# ======================
# DRUM SOUNDS
# ======================

# Kick
kick_env = Adsr(attack=0.001, decay=0.2, sustain=0, release=0.05)
kick = Sine(freq=60, mul=kick_env).out()

# Snare
snare_env = Adsr(attack=0.001, decay=0.1, sustain=0, release=0.05)
snare = Noise(mul=snare_env).out()

# Hi-hat
hihat_env = Adsr(attack=0.001, decay=0.05, sustain=0, release=0.01)
hihat = Noise(mul=hihat_env*0.3).out()

# ======================
# BASS SYNTH
# ======================

bass_env = Adsr(attack=0.01, decay=0.2, sustain=0.4, release=0.1)
bass = SawTable()
bass_osc = Osc(table=bass, freq=55, mul=bass_env*0.4).out()

# ======================
# MELODY SYNTH
# ======================

mel_env = Adsr(attack=0.01, decay=0.2, sustain=0.3, release=0.1)
mel_table = SquareTable()
melody = Osc(table=mel_table, freq=440, mul=mel_env*0.2).out()

notes = [220, 247, 262, 294, 330, 349, 392]

# ======================
# PATTERN EDM
# ======================

kick_pattern  = [1,0,0,0, 1,0,0,0]
snare_pattern = [0,0,1,0, 0,0,1,0]
hihat_pattern = [1,1,1,1, 1,1,1,1]
bass_pattern  = [1,0,1,0, 1,0,1,0]

step = 0

def play():

    global step

    if kick_pattern[step]:
        kick_env.play()

    if snare_pattern[step]:
        snare_env.play()

    if hihat_pattern[step]:
        hihat_env.play()

    if bass_pattern[step]:
        bass_osc.freq = random.choice([55,65,73])
        bass_env.play()

    # melody random
    if random.random() > 0.7:
        melody.freq = random.choice(notes)
        mel_env.play()

    step = (step + 1) % 8

# metronome
metro = Metro(time=beat).play()
TrigFunc(metro, play)

print("EDM generator running...")

s.gui(locals())
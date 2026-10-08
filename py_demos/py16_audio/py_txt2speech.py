import streamlit as st

### StartofFunc###

def pytxt2speech():
    # this is only runable for python3.12 because of pygame
    import io
    import pygame
    from gtts import gTTS

    def speak(text):
        # save sound to RAM
        with io.BytesIO() as file:
            gTTS(text=text, lang="en").write_to_fp(file)
            file.seek(0)
            #Play the sound
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue

    if __name__ == "__main__":
        print("what should I say? ")
        text = input("  >> ")
        speak (text)
### EndofCodeSection###

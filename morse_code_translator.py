class MorseCodeTranslator:
    MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '!': '-.-.--', '@': '.--.-.'
    }
    def __init__(self):
        self.running = True
    
    def text_to_morse(self, text):
        text = text.upper()
        morse_code = ''
        for char in text:
            if char != ' ':
                morse_code += self.MORSE_CODE_DICT.get(char, '') + ' '
            else:
                morse_code += '/ '
        return morse_code.strip()
    
    def run(self):
        print("Morse code translator")
        while self.running:
            text = input("Enter text to translate to Morse Code (or 'exit' to quit): ")
            if text.lower() == 'exit':
                print("Exiting...")
                self.running = False
            else:
                print("Morse Code: ", self.text_to_morse(text))
                
if __name__ == "__main__":
    translator = MorseCodeTranslator()
    translator.run()
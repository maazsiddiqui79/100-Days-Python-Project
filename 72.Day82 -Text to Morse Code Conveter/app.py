from flask import render_template , redirect , url_for , Flask , request



app = Flask(__name__)

MORSE_CODE = {
    # Letters
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    ' ':'/',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

TEXT_CODE = {
    '.-': 'A',    '-...': 'B',    '-.-.': 'C',    '-..': 'D',    '.': 'E',    '..-.': 'F',
    '--.': 'G',    '....': 'H',    '..': 'I',    '.---': 'J',    '-.-': 'K',    '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',    '.--.': 'P',    '--.-': 'Q',    '.-.': 'R',
    '...': 'S',    '-': 'T',    '..-': 'U',    '...-': 'V',    '.--': 'W',    '-..-': 'X',
    '-.--': 'Y',    '--..': 'Z',    
    '/': ' ',
                    
    '-----': '0',    '.----': '1',    '..---': '2',    '...--': '3',    '....-': '4',    '.....': '5',
    '-....': '6',    '--...': '7',    '---..': '8',    '----.': '9'
}





@app.route('/')
def homepage():
    return render_template('home_page.html')


@app.route('/text-to-morse',methods=['GET','POST'])
def text_to_morse():
    MORES_TEXT_LST = []
    MORES_TEXT =''
    if request.method == 'POST':
        text = request.form.get('plaintext')
        print(text)
        for i in text:
            for k,v in MORSE_CODE.items():
                if k.upper() == i.upper():
                    MORES_TEXT_LST.append(v)
                    MORES_TEXT_LST.append(' ')
        MORES_TEXT = MORES_TEXT.join(MORES_TEXT_LST)
        if len(MORES_TEXT )== 0:
            MORES_TEXT = 'INVAILD CHARACTERS'
        
        return render_template('text_to_morse.html',morse_text=MORES_TEXT)
        
    
    return render_template('text_to_morse.html')


@app.route('/morse-to-text',methods=['GET','POST'])
def morse_to_text():
    if request.method == 'POST':
        TEXT= ''
        TEXT_LST = []
        TEXT= ''
        morse_code = request.form.get('morsetext').split(' ')
        # morse_code=morse_code.split(' ')
        for i in morse_code:
            for k , v in TEXT_CODE.items():
                if i==k:
                    TEXT_LST.append(v)
                    
        TEXT = TEXT.join(TEXT_LST)
        if len(TEXT )== 0:
            TEXT = 'INVAILD CHARACTERS'
        return render_template('morse_to_text.html',morse_text=TEXT)
        
    return render_template('morse_to_text.html') 






if __name__ == '__main__':
    app.run(debug=True)
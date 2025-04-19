import random

question_data = [
    {"text": "The first computer programmer was a woman named Ada Lovelace.", "answer": "true"},
    {"text": "The programming language 'Swift' was developed by Microsoft.", "answer": "false"},
    {"text": "The first computer bug was an actual insect.", "answer": "true"},
    {"text": "Java and JavaScript are the same programming language.", "answer": "false"},
    {"text": "Bluetooth technology is named after a 10th-century Scandinavian king.", "answer": "true"},
    {"text": "The first Android smartphone was released before the first iPhone.", "answer": "false"},
    {"text": "The first mechanical computer was designed by Charles Babbage in the 19th century.", "answer": "true"},
    {"text": "HTML is a programming language.", "answer": "false"},
    {"text": "Python was named after the snake species.", "answer": "false"},
    {"text": "Alan Turing is considered the father of modern computing.", "answer": "true"},
    {"text": "The first version of the Mac OS was based on Unix.", "answer": "false"},
    {"text": "The '@' symbol in email addresses was chosen because it was rarely used in computing at the time.", "answer": "true"},
    {"text": "COBOL is a high-level programming language primarily used for scientific computations.", "answer": "false"},
    {"text": "The first mouse was made of wood.", "answer": "true"},
    {"text": "The term 'firewall' in computing originated from firefighting.", "answer": "true"},
    {"text": "The original name of JavaScript was Mocha.", "answer": "true"},
    {"text": "The term 'Wi-Fi' stands for 'Wireless Fidelity'.", "answer": "false"},
    {"text": "The first domain name ever registered was 'symbolics.com'.", "answer": "true"},
    {"text": "The first graphical web browser was Netscape Navigator.", "answer": "false"},
    {"text": "The QWERTY keyboard layout was designed to slow down typing speeds.", "answer": "true"},
    {"text": "The 'C' programming language was developed at Bell Labs.", "answer": "true"},
    {"text": "The first portable computer weighed over 20 pounds.", "answer": "true"},
    {"text": "The first version of the Unix operating system was written in C.", "answer": "false"},
    {"text": "The first electronic computer, ENIAC, was developed during World War II.", "answer": "true"},
    {"text": "The first computer game was 'Pong'.", "answer": "false"},
    {"text": "The term 'spam' for unsolicited emails comes from a brand of canned meat.", "answer": "true"},
    {"text": "SQL stands for Structured Query Language.", "answer": "true"},
    {"text": "The term 'cookie' in computing refers to a small piece of data stored on the user's computer.", "answer": "true"},
    {"text": "The first hard disk drive could store 1 GB of data.", "answer": "false"},
    {"text": "The first email was sent by Ray Tomlinson in 1971.", "answer": "true"},
    {"text": "The first version of Windows was released in 1985.", "answer": "true"},
    {"text": "The first website was created by Tim Berners-Lee in 1991.", "answer": "true"},
    {"text": "The 'Ctrl+Alt+Del' command was originally intended as a security feature.", "answer": "false"},
    {"text": "The first computer virus was created in the 1980s and was called 'Brain'.", "answer": "true"},
    {"text": "The term 'debugging' originated when a moth was found causing issues in an early computer.", "answer": "true"},
    {"text": "FORTRAN is one of the oldest high-level programming languages.", "answer": "true"},
    {"text": "Linux was created by Linus Torvalds in 1991.", "answer": "true"},
    {"text": "RAM stands for Random Access Memory.", "answer": "true"},
    {"text": "The first iPhone was released in 2005.", "answer": "false"},
    {"text": "The term 'robot' was first used in a play by Karel Čapek.", "answer": "true"}
]

random.shuffle(question_data)

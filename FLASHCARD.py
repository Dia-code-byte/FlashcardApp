import tkinter as tk

# Flashcard data (100 general knowledge questions)
flashcards = {
    "What is the capital of France?": "Paris",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the hardest natural substance on Earth?": "Diamond",
    "Which planet is known as the Red Planet?": "Mars",
    "Who was the first President of the United States?": "George Washington",
    "In what year did World War II end?": "1945",
    "What is the boiling point of water in Celsius?": "100",
    "Who invented the telephone?": "Alexander Graham Bell",
    "What is the chemical symbol for gold?": "Au",
    "What is the longest river in the world?": "Nile",
    "Which language has the most native speakers?": "Mandarin Chinese",
    "Who discovered gravity?": "Isaac Newton",
    "What is the tallest mountain in the world?": "Mount Everest",
    "Who is known as the Father of Computers?": "Charles Babbage",
    "Which country is known as the Land of the Rising Sun?": "Japan",
    "How many continents are there?": "7",
    "What is the smallest planet in our solar system?": "Mercury",
    "What is the national animal of India?": "Bengal Tiger",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who was the first man to walk on the moon?": "Neil Armstrong",
    "What gas do plants absorb from the atmosphere?": "Carbon dioxide",
    "Who wrote 'The Origin of Species'?": "Charles Darwin",
    "What is the square root of 64?": "8",
    "Which instrument measures atmospheric pressure?": "Barometer",
    "What is the largest mammal?": "Blue Whale",
    "What is the most spoken language in the world?": "English",
    "Who discovered penicillin?": "Alexander Fleming",
    "Which is the smallest bone in the human body?": "Stapes",
    "How many legs does a spider have?": "8",
    "Which is the fastest land animal?": "Cheetah",
    "Who developed the theory of relativity?": "Albert Einstein",
    "Which is the largest desert in the world?": "Antarctica",
    "What is the capital of Australia?": "Canberra",
    "Who is the author of 'Harry Potter' series?": "J.K. Rowling",
    "Which vitamin is produced when a person is exposed to sunlight?": "Vitamin D",
    "How many teeth does an adult human have?": "32",
    "What is the freezing point of water in Fahrenheit?": "32",
    "What is the main gas found in the air we breathe?": "Nitrogen",
    "What is the tallest animal in the world?": "Giraffe",
    "Which organ purifies blood in the human body?": "Kidneys",
    "Which bird is known for mimicking human speech?": "Parrot",
    "What do bees collect and use to make honey?": "Nectar",
    "What is the first element on the periodic table?": "Hydrogen",
    "Which organ is responsible for pumping blood?": "Heart",
    "Which planet has the most moons?": "Saturn",
    "How many hearts does an octopus have?": "3",
    "What is the capital of Canada?": "Ottawa",
    "What is the largest island in the world?": "Greenland",
    "Who was the first female Prime Minister of India?": "Indira Gandhi",
    "What is the most abundant gas in Earth’s atmosphere?": "Nitrogen",
    "Which country gifted the Statue of Liberty to the USA?": "France",
    "Which is the largest continent?": "Asia",
    "Which month has an extra day in a leap year?": "February",
    "What is the full form of DNA?": "Deoxyribonucleic Acid",
    "What is the name of the fairy in Peter Pan?": "Tinker Bell",
    "Which planet is closest to the sun?": "Mercury",
    "How many bones are there in the adult human body?": "206",
    "Who invented the lightbulb?": "Thomas Edison",
    "Which is the smallest country in the world?": "Vatican City",
    "What does the internet prefix WWW stand for?": "World Wide Web",
    "What is the capital of Brazil?": "Brasília",
    "What is the name of the galaxy we live in?": "Milky Way",
    "What is the name of the longest bone in the human body?": "Femur",
    "Which part of the plant conducts photosynthesis?": "Leaves",
    "Which continent is the Sahara Desert located in?": "Africa",
    "What is the term for animals that eat both plants and meat?": "Omnivores",
    "What is the tallest building in the world as of 2024?": "Burj Khalifa",
    "What is H2O commonly known as?": "Water",
    "Which metal is liquid at room temperature?": "Mercury",
    "What color is the skin of a polar bear under its fur?": "Black",
    "How many players are there in a football (soccer) team?": "11",
    "Which planet is famous for its rings?": "Saturn",
    "What is the name of our natural satellite?": "Moon",
    "How many zeros are there in one million?": "6",
    "What is the capital of Italy?": "Rome",
    "Which gas is essential for human respiration?": "Oxygen",
    "Which animal is known as the King of the Jungle?": "Lion",
    "What is the chemical symbol for Iron?": "Fe",
    "Which fruit is known as the 'king of fruits'?": "Mango",
    "What is the color of chlorophyll?": "Green",
    "Which sport is known as the 'gentleman’s game'?": "Cricket",
    "How many colors are there in a rainbow?": "7",
    "Which sense is associated with the nose?": "Smell",
    "Which country is the Great Wall located in?": "China",
    "What shape is a stop sign?": "Octagon",
    "What is the name of the toy cowboy in Toy Story?": "Woody",
    "Which is the closest star to Earth?": "Sun",
    "What is the process of water turning into vapor called?": "Evaporation",
    "Which instrument has keys, pedals, and strings?": "Piano",
    "Which insect has colorful wings?": "Butterfly",
    "Which bird lays the largest egg?": "Ostrich",
    "Which planet is known for having a Great Red Spot?": "Jupiter",
    "What does a thermometer measure?": "Temperature",
    "Which sea creature has eight legs?": "Octopus",
    "How many days are there in a leap year?": "366",
    "What is the capital of Germany?": "Berlin",
    "What does ATM stand for?": "Automated Teller Machine",
    "Which is the largest internal organ in the human body?": "Liver",
    "Which animal can live both in water and on land?": "Frog",
    "What is the tallest grass in the world?": "Bamboo",
    "What is the main ingredient in bread?": "Flour"
}


root = tk.Tk()
root.title("Flashcard App")
root.geometry("600x400")
root.config(bg="lightyellow")


questions = list(flashcards.keys())
current_question = 0

# Functions
def show_question():
    question_label.config(text=questions[current_question])
    answer_label.config(text="")

def show_answer():
    answer_label.config(text=flashcards[questions[current_question]])

def next_card():
    global current_question
    current_question = (current_question + 1) % len(questions)
    show_question()


question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500, bg="lightyellow")
question_label.pack(pady=30)

answer_label = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="lightyellow")
answer_label.pack(pady=10)

show_answer_btn = tk.Button(root, text="Show Answer", command=show_answer, bg="lightgreen")
show_answer_btn.pack(pady=5)

next_btn = tk.Button(root, text="Next", command=next_card, bg="lightblue")
next_btn.pack(pady=5)

# Start with first question
show_question()

# Run the application
root.mainloop()

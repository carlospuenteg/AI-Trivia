import openai

openai.api_key = "sk-w...lW6" # Get yours here: "https://beta.openai.com/account/api-keys"

#--------------------------------------------

response = openai.Completion.create(
  engine="text-davinci-001",
  prompt="I can ask and answer some difficult general knowledge questions about many types of things.\nQ: What does “www” stand for in a website browser?\nA: World Wide Web\nQ: How long is an Olympic swimming pool (in meters)?\nA: 50 meters\nQ: What countries made up the original Axis powers in World War II?\nA: Germany, Italy, and Japan\nQ: Which country do cities of Perth, Adelade & Brisbane belong to?\nA: Australia\nQ: What geometric shape is generally used for stop signs?\nA: Octagon\nQ: What is \"cynophobia\"?\nA: Fear of dogs\nQ: What punctuation mark ends an imperative sentence?\nA: A period or exclamation point\nQ: Who named the Pacific Ocean?\nA: Ferdinand Magellan\nQ: How many languages are written from right to left?\nA: 12\nQ: How many countries still have Shilling as currency? Bonus point: Which countries?\nA: Four, Kenya, Uganda, Tanzania, and Somalia\nQ: What is the name of the man who launched eBay back in 1995?\nA: Pierre Omidyar\nQ: What is the name of the biggest technology company in South Korea?\nA: Samsung\nQ: Which animal can be seen on the Porsche logo?\nA: Horse\nQ: Which monarch officially made Valentine's Day a holiday in 1537?\nA: Henry VIII\nQ: Who was the first woman to win a Nobel Prize (in 1903)?\nA: Marie Curie\nQ: The first dictionary was written by?\nA: Robert Cawdrey\nQ: Worship of Krishna is observed by which Religious Faith?\nA: Hinduism\nQ: What is the name of the largest ocean on earth?\nA: Pacific Ocean\nQ: Demolition of the Berlin wall separating East and West Germany began in what year?\nA: 1989\nQ: What is the romanized Arabic word for \"moon\"?\nA: Qamar\nQ: Who was the first woman pilot to fly solo across the Atlantic?\nA: Amelia Earhart\nQ:",
  temperature=1,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.7
)

AIResponse = response["choices"][0]["text"].split("\n")
question = AIResponse[0]
answer = AIResponse[1]

#--------------------------------------------

print("Q:" + question)

myAnswer = input("A: ").lower().strip()

#--------------------------------------------

inputPrompt = "Q: Who is the current president of Egypt?\nA: Fattah\nIs this correct?\nYes\nQ: Which Shakespeare play is about two young lovers who are forced to part?\nA: Romeo and Juliet\nIs this correct?\nYes\nQ: What is the capital of the Central African Republic?\nA: Bangi\nIs this correct?\nNo\nQ: What is the name of the largest member of the cat family?\nA: Lion\nIs this correct?\nNo\nQ: What is the name of the largest member of the cat family?\nA: Tiger\nIs this correct?\nYes\nQ: The first successful powered flight was made by which men?\nA: Wright Brothers\nIs this correct?\nYes\nQ: The first successful powered flight was made by which men?\nA: The Wright Brothers\nIs this correct?\nYes" + question + "\nA: " + myAnswer + "\nIs this correct?\n"
isCorrect = openai.Completion.create(
  engine="text-davinci-001",
  prompt=inputPrompt,
  temperature=0,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

AIConfirm = isCorrect["choices"][0]["text"]
confirmation = AIConfirm.lower().strip()

#--------------------------------------------

if confirmation == "yes":
    print("- Correct")
else:
    print("- Incorrect:")
    print(answer)
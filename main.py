import openai

openai.api_key = "sk-w...lW6" # Get yours here: "https://beta.openai.com/account/api-keys"

ENGINE = "text-davinci-001"
INPUT = open("input.txt", "r").read()
CONFIRMATION = open("confirmation.txt", "r").read()
NQUESTIONS = 5

for i in range(1,NQUESTIONS+1):
#-------------------------------------------------------
    response = openai.Completion.create(
    engine=ENGINE,
    prompt=INPUT,
    temperature=0.9,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.7
    )
    AIResponse = response["choices"][0]["text"].split("\n")
    question = AIResponse[0]
    answer = AIResponse[1]
#-------------------------------------------------------
    print(f"{i}. {question}")
    myAnswer = input("Answer: ").strip()
#-------------------------------------------------------
    PROMPT = CONFIRMATION + "Q:" + question + "\nA: " + myAnswer + "\nIs this correct?\n"
    isCorrect = openai.Completion.create(
    engine=ENGINE,
    prompt=PROMPT,
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    AIConfirm = isCorrect["choices"][0]["text"]
    confirmation = AIConfirm.lower().strip()
#-------------------------------------------------------
    if confirmation == "yes":
        print("- Correct")
    else:
        print(f"- Incorrect ({answer[3:]})")
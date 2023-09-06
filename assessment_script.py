import openai

# You'd need to set up your OpenAI API key here
openai.api_key = 'Your api key here'

def evaluate_solution(text):
    # Create the prompt for ChatGPT
    prompt = f"Here are 5 problem description, its right code corrected by the ai model we are going to eveluate and the right version provided by chatgpt. These two versions of the problem are both corrected from the buggy code i provided to them. The two versions of right code might be the same because some problems are too easy to fix. Evaluate the Debugging ability of the genertive Ai and compare its debugging ability with chatgpt's debugging ability and gice a detailed review, make the debugging ability comparsion between ai model and chatgpt and finally give a ovreall score from 0-100, you could take chatgpt as score 80. And please follow 3 criteria to do the assesssment: 1. whether it does the right correction 2. compared to chatgpt's correction, it changed more or less than chatgpt 3. the space and time complexity between chatgpt's right version and its right version. {text}:\n\n"
    
    # Make the API call
    response = openai.Completion.create(
        engine="davinci", 
        prompt=prompt,
        max_tokens=3000
    )
    
    # Extract the assessment from the response
    assessment = response.choices[0].text.strip()
    
    return assessment

def main():
    text = input("Enter the text ")
    
    assessment = evaluate_solution(text)
    print(f"Assessment:\n{assessment}")

if __name__ == "__main__":
    main()

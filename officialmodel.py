import google.generativeai as genai 
import os


class BardGenerator:
    def __init__(self):
        genai.configure(api_key=os.getenv("API_KEY"))
        self.text_model = genai.GenerativeModel("gemini-pro")
        self.image_model = genai.GenerativeModel("gemini-pro-vision")
        self.questions = {}
    
    def format_text(self, text):
        question = text[text.find("Question: ")+len("Question: "):text.find("Answer: ")]
        answer = text[text.find("Answer: ")+len("Answer: "):]
        self.questions[question] = answer

    def generate_questions_from_text_single_word(self, topic, difficulty="college"):
        single_word_response = self.text_model.generate_content(f"Give me a question on the topic {topic} of {difficulty} difficulty which can be answered in a single sentence or word in the following format: \
                                                    Question:  \n Answer: \nDo not put asteriks around the words Question and Answer.")
        text = single_word_response.text
        print(text)
        self.format_text(text)
    def generate_questions_from_text_mcq(self, topic, difficulty="college"):
        mcq_response = self.text_model.generate_content(f"Give me 1 multiple choice question of {difficulty} diifculty with 4 choices on the topic {topic} and the answer to the question in the format: \
                               Question:  \n Answer: \nDo not put asteriks around the words Question and Answer.")
        text = mcq_response.text
        print(text)
        self.format_text(text)
    
    
# bard = BardGenerator() 
# # bard.generate_questions_from_text_single_word("Memory Structure and Architecture")
# bard.generate_questions_from_text_mcq("Memory Structure and Architecture")
# print("\n", bard.questions)

    

# def generate_pair(text):
#     question = text[text.find("Question: ")+len("Question: "):text.find("Answer: ")]
#     answer = text[text.find("Answer: ")+len("Answer: "):]

# questions = {}
# topic = "Memory Structure and Architecture"
# difficulty = "hard"
# genai.configure(api_key=os.getenv("API_KEY"))

# text_model = genai.GenerativeModel('gemini-pro')

# mcq_response = text_model.generate_content(f"Give me 1 multiple choice question of {difficulty} with 4 choices on the topic {topic} and the answer to the question in the format: \
#                                Question: *Question*\n Answer: *Answer*. Do not put asteriks around the words Question and Answer.")
# single_word_response = text_model.generate_content(f"Give me a question on the topic {topic} of {difficulty} difficulty which can be answered in a single sentence or word in the following format: \
#                                               Question: *Question* \n Answer: *Answer*. Do not put asteriks around the words Question and Answer.")
# text = single_word_response.text
# print(text)


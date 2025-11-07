import random
import os

class CountryQuiz:
    def __init__(self, p_question_number, p_num_of_students, file_name):
        self.p_question_number = p_question_number
        self.p_num_of_students = p_num_of_students
        self.file_name = file_name
        self.dict={}
        
    @staticmethod
    def get_int(prompt):
        while True:
            try:
                choice = int(input(prompt))
                return choice
            except ValueError:
                print('Invalid Input')

    @staticmethod
    def delete_files():
        for file in os.listdir():
            if file.endswith('.txt') and not(file.startswith('country')):
                os.unlink(file)
    
    def parsed_dict(self):
        with open(self.file_name, 'r', encoding='utf-8') as country_file:
            country_file.readline()
            for country_info in country_file:
                info_list = country_info.strip().split(';')
                if len(info_list)>=3:
                    name, capital = info_list[1], info_list[2]
                    self.dict[name.strip()] = capital.strip()

            return True
        

    def question_maker(self, correctAnswer_list=None, seq_num = 1, question_seq = 0, option_numbers = 4):
        if correctAnswer_list is None:
            correctAnswer_list = []

        for _ in range(self.p_num_of_students):
            with open('question.txt'if seq_num == 0 else f'question{seq_num}.txt', 'w') as question_file:
                seq_num +=1
                question_file.write('Name:\n\nDate:\n\n')
                question_file.write(' '*20 +'TEST YOUR KNOWLEDGE ABOUT COUNTRIES AND THEIR CAPITALS')
                question_file.write('\n\n')
                countries_list = list(set(self.dict.keys()))
                random.shuffle(countries_list)
                question_seq = 0
                for _ in range(self.p_question_number):
                    country = countries_list[question_seq]
                    correctAnswer = self.dict[country]
                    wrongAnswers = list(set(self.dict.values()))
                    del wrongAnswers[wrongAnswers.index(correctAnswer)]
                    wrongAnswers = random.sample(wrongAnswers, option_numbers-1)
                    answerOptions = wrongAnswers + [correctAnswer]
                    random.shuffle(answerOptions)
                    question_file.write(f'\n{question_seq+1}. What is the Capital City Of {country}: \n\n')
                    for options in range(option_numbers):
                        question_file.write(' '*5 + f'{"ABCD"[options]}.'+ f' {answerOptions[options]}\n')
                        question_file.write('\n\n')
                    correctAnswer_list.append(answerOptions.index(correctAnswer))
                    question_seq +=1
                    
        return correctAnswer_list
                

    def get_answers(self, indexlist, seq_num = 0):
        for _ in range(self.p_num_of_students):
            with open(f'answer{seq_num+1}.txt', 'w') as answer_file:
                seq_num+=1
                answer_file.write(" "*20 + 'QUIZ ANSWERS\n\n')
                for number in range(self.p_question_number):
                    answer_file.write(' '*5+f'{number+1}. {'ABCD'[indexlist[0]]}\n\n')
                    del indexlist[0]


def main():
    """Displays CLI interface for users to interact with app"""

    print('\n============== WELCOME TO THE COUNTRY QUIZ APP ====================')
    question_number = CountryQuiz.get_int('\nEnter number of questions: ')
    number_of_files = CountryQuiz.get_int('\nEnter number of students: ')
    CountryQuiz.delete_files()
    country = CountryQuiz(question_number, number_of_files, 'country_data.txt')
    country.parsed_dict()
    indexlist = country.question_maker()
    country.get_answers(indexlist)

if __name__ == '__main__':
    main()
from fileinput import filename
import pathlib as pl

class CountryQuiz:
    def __init__(self, p_q_number, p_num_of_files, file_name):
        self.p_number =p_q_number
        self.p_num_of_files =p_num_of_files
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
    
    def parsed_dict(self):
        with open(self.file_name, 'r', encoding='utf-8') as country_file:
            country_file.readline()
            for country_info in country_file:
                info_list = country_info.strip().split(';')
                name, capital = info_list[1:3]
                self.dict[name] = capital
            return
                

            


def main():

    print('\n============== WELCOME TO THE COUNTRY QUIZ APP ====================')
    question_number = CountryQuiz.get_int('\nEnter number of questions: ')
    number_of_files = CountryQuiz.get_int('\nEnter number of students: ')
    country = CountryQuiz(question_number, number_of_files, 'country_data.txt')
    parsed_dict = country.parsed_dict()

if __name__ == '__main__':
    main()
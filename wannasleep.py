
import sys
from stackapi import StackAPI
import os

search_string = 'typeerror: list indices must be integers or slices, not str'

SITE = StackAPI('stackoverflow')

class Scarpper():
  def __init__(self, search_string):
    self.SITE = StackAPI('stackoverflow')
    self.search_string = search_string
    self.question_id = self.get_question()

  def get_question(self):
    questions = SITE.fetch('search/advanced', title = self.search_string)

    answered_questions = []

    question_id = int()

    for q in questions['items']:  
      if q['is_answered'] == True:
        answered_questions.append(q)
        scores = [question['score'] for question in answered_questions]
        for question in answered_questions:
          if question['score'] == max(scores):
            question_id = question['question_id']
            break
    
    return question_id
  
  
  def display_answer(self):

    if self.question_id > 0: 
      answers = SITE.fetch('questions/{ids}/answers', ids=self.question_id, filter='withbody')
      for a in answers['items']:
        if a['is_accepted'] == True:
          answer = a['body']
          break

      with open('answer.html', 'w') as f:
        f.write(answer)
        
      os.system('firefox answer.html')

    else:
      print("No answer was found")
      sys.exit()

Scarpper(search_string).display_answer()
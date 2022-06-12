
from stackapi import StackAPI
import sys
import os
import html2text

SITE = StackAPI('stackoverflow')

class Scrapper():
  def __init__(self, search_string):
    self.SITE = StackAPI('stackoverflow')
    self.search_string = search_string
    self.question_id = self.get_question()

  def get_question(self):
    questions = SITE.fetch('search/advanced', title = self.search_string)

    answered_questions = []

    question_id = int()

    #best question selection
    
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
      
      #best answer slection
      
      for a in answers['items']:
        if a['is_accepted'] == True:
          answer = a['body']
          break
      
      print(html2text.html2text(answer))

    else:
      print("No answer was found")
      sys.exit()

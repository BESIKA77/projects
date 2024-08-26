while True:
   print('hello to movie guess! today i will guess your movie!')
   print('wish one of that movie: harry potter, pirates of caribbean, hobbit, lucifer, cobra kai.')
   question_1 = input('Are there magic wands in your movie?(yes or no): ')
   if question_1 == 'yes':
       question_2_of_1 = input('Is the main character cursed?: ')
       if question_2_of_1 == 'yes':
           print('i know! its harry potter!')
           quit_1 = input('do u want to quit or play again?')
           if quit_1 == 'quit':
              quit()
           elif quit_1 == 'play again':
               print('playing again')
       elif question_2_of_1 == 'no':
           question_1_of_2 = input('Do kids learn karate in this movie? ')
           if question_1_of_2 == 'yes':
               question_2_of_2 = input('Does anyone in this movie have a tattoo of a hawk on their back? ')
               if question_2_of_2 == 'yes':
                   print('I know! its cobra kai!')
                   quit_1 = input('do u want to quit or play again?')
                   if quit_1 == 'quit':
                      quit()
                   elif quit_1 == 'play again':
                      print('playing again')
               elif question_2_of_2 == 'no':
                   question_1_of_3 = input('Does this movie take place in the sea? ')
                   if question_1_of_3 == 'yes':
                       question_2_of_3 = input('Is the movie about pirates? ')
                       if question_2_of_3 == 'yes':
                          print('i know!its pirates of carribean!')
                          quit_1 = input('do u want to quit or play again?')
                          if quit_1 == 'quit':
                            quit()
                          elif quit_1 == 'play again':
                            print('playing again')
                       elif question_2_of_3 == 'no':
                           question_1_of_4 = input('Did the dragon destroy the kingdom in this movie? ')
                           if question_1_of_4 == 'yes':
                               question_2_of_4 = input('Are there gnomes, witches, elves and such creatures in this movie? ')
                               if question_2_of_4 == 'yes':
                                   question_3_of_4 = input('Does the magician take the main character on an adventure? ')
                                   if question_3_of_4 == 'yes':
                                       print('i know!its hobbit!')
                                       quit_1 = input('do u want to quit or play again?')
                                       if quit_1 == 'quit':
                                         quit()
                                       elif quit_1 == 'play again':
                                         print('playing again')
                                   elif question_3_of_4 == 'no':
                                       question_1_of_5 = input('Is the main character a devil? ')
                                       if question_1_of_5 == 'yes':
                                           print('I know!Its lucifer!')
                                           quit_1 = input('do u want to quit or play again')
                                           if quit_1 == 'quit':
                                              quit()
                                           elif quit_1 == 'play again':
                                              print('playing again')
                                       elif question_1_of_5 == 'no':
                                          question_2_of_5 = input('Does the movie feature a cursed crew of undead pirates?')
                                          if question_2_of_5 == 'yes':
                                              print('I know! Its pirates of caribean!')
                                              quit_1 = input('do u want to quit or play again?')
                                              if quit_1 == 'quit':
                                                 quit()
                                              elif quit_1 == 'play again':
                                                print('playing again')
                                          elif question_2_of_5 == 'no':
                                              question_3_of_5 = input('Does the show feature a karate dojo led by a character named Johnny Lawrence? ')
                                              if question_3_of_5 == 'yes':
                                                   print('I know! Its cobra kai!')
                                                   quit_1 = input('do u want to quit or play again?')
                                                   if quit_1 == 'quit':
                                                      quit()
                                                   elif quit_1 == 'play again':
                                                      print('playing again')
                                              elif question_3_of_5 == 'no':
                                                 again_or_not = input('there are no more questions! do you want to play again or quit? ')
                                                 if again_or_not == 'quit':
                                                    quit()
                                                 elif again_or_not == 'play again':
                                                    print('playing again')
                   elif question_1_of_3 == 'no':
                      question_1_of_6 = input('Does the movie series feature a school of magic called Hogwarts?')
                      if question_1_of_6 == 'yes':
                         print('I know! Its harry potter! ')
                         quit_1 = input('do u want to quit or play again')
                         if quit_1 == 'quit':
                             quit()
                         elif quit_1 == 'play again':
                            print('playing again')
                            if question_1_of_6 == 'no':
                                again_or_not = input('there are no more questions! do you want to play again or quit? ')
                                if again_or_not == 'quit':
                                    quit()
                                elif again_or_not == 'play again':
                                  print('playing again')
           elif question_1_of_2 == 'no':
              question_2_of_6 = input('Does the protagonist of the show work as a consultant for the LAPD while grappling with his identity and past? ')
              if question_2_of_6 == 'yes':
                  question_3_of_6 = input('Does the show feature a character who has the ability to compel people to reveal their deepest desires and truths? ')
                  if question_3_of_6 == 'yes':
                     print('I know! Its lucifer!')
                     uit_1 = input('do u want to quit or play again')
                     if quit_1 == 'quit':
                         quit()
                     elif quit_1 == 'play again':
                        print('playing again')
                  elif question_3_of_6 == 'no':
                     again_or_not = input('there are no more questions! do you want to play again or quit? ')
                     if again_or_not == 'quit':
                         quit()
                     elif again_or_not == 'play again':
                          print('playing again')
   elif question_1 == 'no':
      question_4_of_6 = input('Does the story involve a quest to reclaim a lost kingdom from a dragon named Smaug? ')
      if question_4_of_6 == 'yes':
          print('I know! Its Hobbit!')
          quit_1 = input('do u want to quit or play again?')
          if quit_1 == 'quit':
             quit()
          elif quit_1 == 'play again':
            print('playing again')
      elif question_4_of_6 == 'no':
         question_5_of_6 = input('Is the show set in a world where two rival karate dojos are led by former competitors from a 1980s martial arts film? ')
         if question_5_of_6 == 'yes':
             print('I know! Its Cobra kai!')
             quit_1 = input('do u want to quit or play again?')
             if quit_1 == 'quit':
                quit()
             elif quit_1 == 'play again':
                print('playing again')
         elif question_5_of_6 == "no":
            question_3_of_4 = input('Does the magician take the main character on an adventure? ')
            if question_3_of_4 == 'yes':
               print('i know!its hobbit!')
               quit_1 = input('do u want to quit or play again?')
               if quit_1 == 'quit':
                  quit()
               elif quit_1 == 'play again':
                  print('playing again')
            elif question_3_of_4 == 'no':
               question_1_of_5 = input('Is the main character a devil? ')
               if question_1_of_5 == 'yes':
                   print('I know!Its lucifer!')
                   quit_1 = input('do u want to quit or play again')
                   if quit_1 == 'quit':
                     quit()
                   elif quit_1 == 'play again':
                    print('playing again')
               elif question_1_of_5 == 'no':
                  question_2_of_5 = input('Does the movie feature a cursed crew of undead pirates?')
                  if question_2_of_5 == 'yes':
                      print('I know! Its pirates of caribean!')
                      quit_1 = input('do u want to quit or play again?')
                      if quit_1 == 'quit':
                        quit()
                      elif quit_1 == 'play again':
                        print('playing again')
                  elif question_2_of_5 == 'no':
                        question_3_of_5 = input('Does the show feature a karate dojo led by a character named Johnny Lawrence? ')
                        if question_3_of_5 == 'yes':
                           print('I know! Its cobra kai!')
                           quit_1 = input('do u want to quit or play again?')
                           if quit_1 == 'quit':
                              quit()
                           elif quit_1 == 'play again':
                              print('playing again')
                        elif question_3_of_5 == 'no':
                           again_or_not = input('there are no more questions! do you want to play again or quit? ')
                           if again_or_not == 'quit':
                             quit()
                           elif again_or_not == 'play again':
                              print('playing again')
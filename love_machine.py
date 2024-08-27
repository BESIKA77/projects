while True:
   print('hello, this is love machine!')
   same_answer = 0
   gender_choise = input('please enter your gender: ')
   
   if gender_choise == 'boy':
       boy_name = input('enter your name: ')
       print('hello ' + boy_name + ', please answer some simple questions:')
       boy_fav_color = input('enter your favorite color: ')
       boy_fav_animal = input('enter your favorite animal: ')
       boy_fav_letter = input('enter your favorite letter: ')
       boy_fav_sport = input('enter your favorite sport: ')
       boy_fav_county =  input('enter your favorite country: ')
       boy_fav_movie = input('enter your favorite movie: ')
       boy_fav_food = input('enter your favorite food: ')
       boy_fav_hobby = input('enter your favorite hobby: ')
       boy_ex_number = int(input('enter your ex''s' ' number: '))
       boy_fav_academy = input('enter your favorite academy: ')
   elif gender_choise == 'girl':
       girl_name = input('enter your name: ')
       print('hello ' + girl_name + ', please answer some simple questions:')
       girl_fav_color = input('enter your favorite color: ')
       girl_fav_animal = input('enter your favorite animal: ')
       girl_fav_letter = input('enter your favorite letter: ')
       girl_fav_sport = input('enter your favorite sport: ')
       girl_fav_county =  input('enter your favorite country: ')
       girl_fav_movie = input('enter your favorite movie: ')
       girl_fav_food = input('enter your favorite food: ')
       girl_fav_hobby = input('enter your favorite hobby: ')
       girl_ex_number = int(input('enter your ex''s' ' number: '))
       girl_fav_academy = input('enter your favorite academy: ')
   elif gender_choise != 'boy' and gender_choise != 'girl':
       print('other genders dont know what is love')



   if gender_choise == 'boy':
      opposite_gender = 'girl'
      print("its girl's turn! lets answer qustions again!")
      girl_name = input('enter your name: ')
      girl_fav_color = input('enter your favorite color: ')
      girl_fav_animal = input('enter your favorite animal: ')
      girl_fav_letter = input('enter your favorite letter: ')
      girl_fav_sport = input('enter your favorite sport: ')
      girl_fav_county =  input('enter your favorite country: ')
      girl_fav_movie = input('enter your favorite movie: ')
      girl_fav_food = input('enter your favorite food: ')
      girl_fav_hobby = input('enter your favorite hobby: ')
      girl_ex_number = int(input('enter your ex''s' ' number: '))
      girl_fav_academy = input('enter your favorite academy: ')


   if gender_choise == 'girl':
      opposite_gender = 'boy'
      print("its boy's turn! lets answer qustions again!")
      boy_name = input('enter your name: ')
      boy_fav_color = input('enter your favorite color: ')
      boy_fav_animal = input('enter your favorite animal: ')
      boy_fav_letter = input('enter your favorite letter: ')
      boy_fav_sport = input('enter your favorite sport: ')
      boy_fav_county =  input('enter your favorite country: ')
      boy_fav_movie = input('enter your favorite movie: ')
      boy_fav_food = input('enter your favorite food: ')
      boy_fav_hobby = input('enter your favorite hobby: ')
      boy_ex_number = int(input('enter your ex''s' ' number: '))
      boy_fav_academy = input('enter your favorite academy: ')


   if girl_fav_color == boy_fav_color and boy_fav_color == girl_fav_color:
       same_answer += 1

   if girl_fav_animal == boy_fav_animal and boy_fav_animal == girl_fav_animal:
       same_answer += 1

   if girl_fav_letter == boy_fav_letter and boy_fav_letter == girl_fav_letter or girl_fav_letter == boy_name[0] or boy_fav_letter == girl_name[0]:
       same_answer += 1

   if girl_fav_sport == boy_fav_sport and boy_fav_sport == girl_fav_sport:
       same_answer += 1

   if girl_fav_county == boy_fav_county and boy_fav_county == girl_fav_county:
       same_answer += 1

   if girl_fav_movie == boy_fav_movie and boy_fav_movie == girl_fav_movie:
       same_answer += 1

   if girl_fav_food == boy_fav_food and boy_fav_food == girl_fav_food:
       same_answer += 1

   if girl_fav_hobby == boy_fav_hobby and boy_fav_hobby == girl_fav_hobby:
       same_answer += 1

   if girl_ex_number == boy_ex_number and boy_ex_number == girl_ex_number:
       same_answer += 1
   elif girl_ex_number > boy_ex_number or boy_ex_number > girl_ex_number:
       same_answer -= 1

   if boy_fav_academy == girl_fav_academy and girl_fav_academy == boy_fav_academy:
       same_answer += 1
   elif boy_fav_academy != 'GOA' or boy_fav_academy != 'goa' or boy_fav_academy != 'Goa' and girl_fav_academy != 'GOA' or girl_fav_academy != 'goa' or girl_fav_academy != 'Goa':
       same_answer - 9
       print('leave him/her')
       break

   percent = ((same_answer/10) * 100)
   print('You got ' + str(same_answer) + ' same answer!')   
   print('You got ' + str(percent) + ' percent of same answers') 


   if percent == 0:
       print('ypu are terible couple!')
       choise = input('enter if you want to stay or leave: ')
       if choise == 'quit':
           print('goodbye :)')
           quit()
       elif choise == 'stay':
           print('*playing again:*')

   elif percent <= 50:
       print('you are not good couple!')
       choise = input('enter if you want to stay or leave: ')
       if choise == 'quit':
           print('goodbye :)')
           quit()
       elif choise == 'stay':
           print('*playing again:*')

   elif percent > 50 and percent <= 70:
       print('good couple!')
       choise = input('enter if you want to stay or leave: ')
       print('goodbye :)')
       if choise == 'quit':
           quit()
       elif choise == 'stay':
           print('*playing again:*')
           
   elif percent > 70 and percent <= 100:
       print(boy_name + ', ' + girl_name + ', ' 'you are best couple!')
       choise = input('enter if you want to stay or leave: ')
       if choise == 'quit':
           print('goodbye :)')
           quit()
       elif choise == 'stay':
           print('*playing again:*')
           
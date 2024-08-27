
Initial_budget = 0
withdraw = int(input('enter how much monwy do u want to deposit: '))
Initial_budget = Initial_budget + withdraw
while True:
   print('welcome to myauto! look at car list and choose what car do you want to buy')
   cars = ['toyota', 'BMW', 'Mercedes', 'Honda', 'Nissan', 'porche', 'Mclaren', 'suzuki', 'opel']
   print(cars)
   choose = input('please enter car: ').capitalize()
   if choose == 'Toyota':
       toyota_model_list = ['supra', 'camry', 'prius', 'Land cruiser']
       print(toyota_model_list)
       toyota_model = input('enter toyota model: ')
       if toyota_model == 'supra':
           print('5 left')
           supra = ['toyota supra mk 4 orange and green', 'toyota supra mk 4 white', 'toyota supra mk 5 red,', 'toyota supra mk 3 white', 'toyota supra mk 5 black']
           print(supra)
           supra_choice = input('enter one of that supra to see more information: ' )
           if supra_choice == supra[0] or supra_choice == '1':
               print('date:1995')
               print('engine:2JZ-GTE 3.0-liter turbocharged inline-6')
               print('mileage:100000km')
               print('price:150,000')
               supra_price = 150000
               final_choise = input('do you want to buy this car? ')
               if final_choise == 'yes':
                   if Initial_budget > supra_price:
                      Initial_budget = Initial_budget - supra_price
                      print('congrats! you buy this car for 150,000$. you left' + str(Initial_budget))
                   elif Initial_budget < supra_price:
                       print('you dont have enough money! you can visit bank and withdraw money ')
                       quit()
               elif final_choise == 'no':
                   print('ok,lets check other supras')
                   print(supra)
                   supra_choice = input('enter one of that supra to see more information: ' )
                   if supra_choice == supra[1]  or supra_choice == '2':
                       print('date:1995')
                       print('engine:2JZ-GTE 3.0-liter turbocharged inline-6')
                       print('mileage:100000km')
                       print('price:100,000')
                       supra_2_price = 100000
                       final_choise = input('do you want to buy this car? ')
                       if final_choise == 'yes':
                          if Initial_budget > supra_2_price:
                               Initial_budget = Initial_budget - supra_2_price
                               print('congrats! you buy this car for 100,000$. you left' + str(Initial_budget))
                          elif Initial_budget < supra_2_price:
                            print('you dont have enough money! you can visit bank and withdraw money')
                            quit()
                       elif final_choise == 'no':
                           print('ok,lets check other supras')
                           print(supra)
                           supra_choice = input('enter one of that supra to see more informationz; ')
                           if supra_choice == supra[2]  or supra_choice == '3':
                               print('date:2019')
                               print('engine: a turbocharged B48 2.0-litre inline-four or a turbocharged B58 3.0-litre inline-six')
                               print('mileage:100000km')
                               print('price:110,000')
                               supra_3_price = 110000
                               final_choise = input('do you want to buy this car? ')
 
                               if final_choise == 'yes':
                                  if Initial_budget > supra_3_price:
                                     Initial_budget = Initial_budget - supra_3_price
                                     print('congrats! you buy this car for 110,000$. you left' + str(Initial_budget))
                                  elif Initial_budget < supra_3_price:
                                    print('you dont have enough money! you can visit bank and withdraw money ')
                                    quit()
                               elif final_choise == 'no':
                                   print('ok,lets check other supras')
                                   print(supra)
                                   supra_choice = input('enter one of that supra to see more information: ')
                                   if supra_choice == supra[3]  or supra_choice == '4':
                                    print('date:1986')
                                   print('engine: 3.0-liter 7M-GTE turbocharged inline-six')
                                   print('mileage:130000km')
                                   print('price:21000')
                                   supra_4_price = 21000
                                   final_choise = input('do you want to buy this car? ')
                                   if final_choise == 'yes':
                                       if Initial_budget > supra_4_price:
                                           Initial_budget = Initial_budget - supra_4_price
                                           print('congrats! you buy this car for 21,000$. you left' + str(Initial_budget))
                                       elif Initial_budget < supra_4_price:
                                           print('you dont have enough money! you can visit bank and withdraw money ')
                                           quit()
                                   elif final_choise == 'no':
                                       print('ok,lets check other supras')
                                       print(supra)
                                       supra_choice = input('enter one of that supra to see more information: ' )
                                       if supra_choice == supra[4]  or supra_choice == '5':
                                           print('date:2019')
                                           print('engine: a turbocharged B48 2.0-litre inline-four or a turbocharged B58 3.0-litre inline-six')
                                           print('mileage:130000km')
                                           print('price:215000')
                                           supra_5_price = 215000
                                           final_choise = input('do you want to buy this car? ')

                                           if final_choise == 'yes':
                                              if Initial_budget > supra_5_price:
                                                   Initial_budget = Initial_budget - supra_5_price
                                                   print('congrats! you buy this car for 215000$. you lost' + str(Initial_budget))
                                              elif Initial_budget < supra_5_price:
                                                  print('you dont have enough money! you can visit bank and withdraw money ')
                                                  quit()
                                           elif final_choise == 'no':
                                                   print('there are no more supras,lets check other toyota''s')
                                                   print(toyota_model_list)



# working on it
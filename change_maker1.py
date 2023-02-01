nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0
stocks = [quarters, dimes, nickels]
pick = ['n', 'd', 'q', 'o', 'f', 'c']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
quarters_change = 0
dimes_change = 0
nickels_change = 0
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
print(f'Stock contains:\n   {nickels} nickels\n   {dimes} dimes\n   {quarters} quarters\n   {ones} ones\n   {fives} fives\n')
option = input("Enter the purchase price (xx.xx) or `q' to quit: ")

if option == 'q':
    print(f"Total: {(nickels * 5 + dimes * 10 + quarters * 25 + ones * 100 + fives * 500) // 100} dollars and {(nickels * 5 + dimes * 10 + quarters * 25 + ones * 100 + fives * 500) - (100 * (nickels * 5 + dimes * 10 + uarters * 25 + ones * 100 + fives * 500) // 100)} cents")

else:
    while option != 'q':
        if option not in number:
            print("Invalid purchase price. Try again")
        count = 0
        for a in range(len(option)):
            if option[a] == '.':
                count += 1
        i=0
        while i < len(option):
            if option[i] not in num or option[i] == "-" or count > 1:
                print('Invalid purchase price. Try again')
            i += 1
            break

        if i == len(option):
            if option[0] not in number or option == '.':
                print("Invalid purchase price. Try again")
            elif option[0] == "-":
                b = 1
                while b < len(option):
                    if option[b] not in number:
                        print('Invalid purchase price. Try again')
                    i += 1
                    break
                print("Illegal price: Must be a non-negative multiple of 5 cents.")

            else:
                purchase=float(option)*100
                if purchase % 5 != 0 or purchase == 0:
                    print('Illegal price: Must be a non-negative multiple of 5 cents.')
                else:
                    print("Menu for deposits:")
                    print("   'n' - deposit a nickel")
                    print("   'd' - deposit a dime")
                    print("   'q' - deposit a quarter")
                    print("   'o' - deposit a one dollar bill")
                    print("   'f' - deposit a five dollar bill")
                    print("   'c' - cancel the purchase\n")
                    indi = 0
                    payment = int(purchase)

                    while payment >= 0:
                        if int(payment) >= 100:
                            print(f'Payment due: {payment // 100} dollars and {payment % 100} cents')
                        else:
                            print(f'Payment due: {payment} cents')
                        indi = input("Indicate your deposit: ")

                        if indi not in pick:
                            print(f'Illegal selection: {indi}')
                        else:
                            if indi == 'n':
                                payment -= 5
                                nickels += 1
                            elif indi == 'd':
                                payment -= 10
                                dimes += 1
                            elif indi == 'q':
                                payment -= 25
                                quarters += 1
                            elif indi == 'o':
                                payment -= 100
                                ones += 1
                            elif indi == 'f':
                                payment -= 500
                                fives += 1

                            if payment < 0:
                                change_left = abs(payment_due)
                                while quarters > 0 and change_left >= 25:
                                    change_left -= 25
                                    quarters_change += 1
                                    quarters -= 1
                                while dimes > 0 and change_left >= 10:
                                    change_left -= 10
                                    dimes_change += 1
                                    dimes -= 1
                                while nickels > 0 and change_left >= 5:
                                    change_left -= 5
                                    nickels_change += 1
                                    nickels -= 1
                                print('Please take the change below.')

                                if change_left == 0:
                                    if quarters_change > 0:
                                        print(f'   {quarters_change} quarters')
                                    if dimes_change > 0:
                                        print(f'   {dimes_change} dimes')
                                    if nickels_change > 0:
                                        print(f'   {nickels_change} nickels')

                                elif change_left > 0:
                                    if quarters_change > 0:
                                        print(f'   {quarters_change} quarters')
                                    if dimes_change > 0:
                                        print(f'   {dimes_change} dimes')
                                    if nickels_change > 0:
                                        print(f'   {nickels_change} nickels')
                                    print('Machine is out of change.\nSee store manager for remaining refund.')

                                    if change_left >= 100:
                                        print(f'Amount due: {(change_left - quarters_change * 25 - dimes_change * 10 - nickels_change * 5) // 100} dollars and {(change_left - quarters_change * 25 - dimes_change * 10 - nickels_change * 5) % 100} cents')
                                    else:
                                        print(f'Amount due: {(change_left - quarters_change * 25 - dimes_change * 10 - nickels_change * 5) % 100} cents')
                                print(f'\nStock contains:\n   {nickels} nickels\n   {dimes} dimes\n   {quarters} quarters\n   {ones} ones\n   {fives} fives\n')
                                break

                            if payment == 0:
                                print('Please take the change below.')
                                print('   No change due.')
                                print(f'Stock contains:\n   {nickels} nickels\n   {dimes} dimes\n   {quarters} quarters\n   {ones} ones\n   {fives} fives\n')
                                break

                            if indi == 'c':
                                change_left = int(purchase) - payment
                                while quarters > 0 and change_left >= 25:
                                    change_left -= 25
                                    quarters_change += 1
                                    quarters -= 1
                                while dimes > 0 and change_left >= 10:
                                    change_left -= 10
                                    dimes_change += 1
                                    dimes -= 1
                                while nickels > 0 and change_left >= 5:
                                    change_left -= 5
                                    nickels_change += 1
                                    nickels -= 1
                                print('Please take the change below.')
                                if quarters_change > 0:
                                    print(f'   {quarters_change} quarters')
                                if dimes_change > 0:
                                    print(f'   {dimes_change} dimes')
                                if nickels_change > 0:
                                    print(f'   {nickels_change} nickels')

                                if change_left > 0:
                                    print('Machine is out of change.\nSee store manager for remaining refund.')
                                    if change_left >= 100:
                                        print(f'Amount due: {(purchase - payment_due - ((quarters_change * 25) + (dimes_change * 10) + (nickels_change * 5))) // 100} dollars and {(purchase - payment_due - (quarters_change * 25 + dimes_change * 10 + nickels_change * 5)) % 100} cents')
                                    else:
                                        print(f'Amount due: {((purchase * 100) - payment_due - (quarters_change * 25 + dimes_change * 10 + nickels_change * 5)) % 100} cents')
                                print(f'\nStock contains:\n   {num_nickels} nickels\n   {num_dimes} dimes\n   {num_quarters} quarters\n   {num_ones} ones\n   {num_fives} fives\n')
                                break

        choice = input("Enter the purchase price (xx.xx) or `q' to quit: ")

# 1.derste print() kullanımı anlatiliyor ve alınmak istenen çıktıları her egzersiz için yorum satırı oluşturup yazdım. 

#exercise1 (Printing) çıktıları:

# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


#exercise2 (Debugging Practice) çıktıları:

# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.
print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
# \n ve + kullanarak bir şeyler yazmayı deneyelim :)
print("Hello " + "Zeynep\n" + "Welcome " + "to " + "my " + "country")

#exercise3 (Input Function) çıktıları:

# NOT: kullanıcıdan yanıt almak için print() yerine input() kullanılır.
# 3. egzersizde bizden kullanıcının ismini alıp harf sayısının kod tarafından bize verilmesi isteniyor.

print(len(input("What is your name? ")))

#exercise4 (Cariables) çıktıları:
# Kullanıcıdan a ve b harflerine sayı atamaları isteniyor. Çıktı olarak ise bunların yerlerinin değiştirilmesi gerekiyor.

a = input("a: ")
b = input("b: ")

# yeni bir harf tanımlanarak bu a'ya eşitlenir. a ise b'ye ve son olarak b de c'ye eşitlenir.
# bu sayede a b'ye, b'de a'ya dönüşmüş olur.
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# a = int(input("첫번째 숫자 입력: "))
# b = int(input("두번째 숫자 입력: "))
# print(a + b)

# # 숫자 하나를 입력받아서
# # 짝수면 짝수입니다
# # 홀수면 홀수입니다
# # 를 출력하는 프로그램을 작성하시오.
# number = int(input("숫자 입력 :"))
# if number % 2 == 0 :
#     print("짝수입니다.")
# else :
#     print("홀수입니다.")

# number = int(input("숫자 입력 :"))
# if number > 0 :
#     print("양수")
# elif number == 0 :
#     print("0")
# elif number < 0 :
#     print("음수")

# num = int(input("숫자 입력 :"))
# total = 0
# for i in range(1,num + 1) :
#     total = total + i
# print(total)

# nums = [1, 4, 7, 10, 13, 16]
# for i in nums :
#     if i % 2 == 0 :
#         print(i)

# nums = [2, 6, 3, 9, 1, 10] #[6,9,10]
# result = []
# for i in nums :
#     if i > 5 :
#         result.append(i)
# print(result)

# word = "education" #euaio
# result = ""
# string = "euaio"

# for i in word :
#     if i in string :
#         result = result + str(i)
# print(result)

# nums = [1, 3, 5, 7, 9] # 문제 1
# result = []
# for i in nums :
#     if i % 2 != 0 :
#         result.append(i)
# print(result)

# word = "banana" # 문제 2 "aaa"
# result = ""
# for i in word :
#     if i == "a" :
#         result = result + i
# print(result)

# nums = [1, 2, 3, 4, 5, 6] # 문제 3 [2, 4, 6]
# result = []
# for i in nums :
#     if i % 2 == 0 :
#         result.append(i)
# print(result)


# nums = [3, 7, 2, 9, 4] # 짝수의 합 구하기 6
# result = 0
# for i in nums :
#     if i % 2 == 0:
#         result +=i
# print(result)

def even_sum(nums): #print(even_sum([1, 2, 3, 4, 5, 6])) 12
    result = 0
    for i in nums :
        if i % 2 == 0 :
           result += i
    return result
print(even_sum([1, 2, 3, 4, 5, 6]))


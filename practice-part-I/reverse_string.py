# # # print("Hello's world")
# # # print('He\'s good guy')
# #
# # def reverse(s):
# #     str = " "
# #     for i in s:
# #         str = i + str
# #         print(str)
# #     return str
# #
# #
# # s = "Payel"
# #
# # print("Original string is : ", end=" ")
# # print(s)
# #
# # print("The resversed string is ", end=" ")
#
# # print(reverse(s))
#
#
# def reverse_slicing(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_slicing(s[1:]) + s[0]
#
#
# s = "Welcome"
# print(reverse_slicing(s))

s = "Payel"
str = s[1:]
print(str)

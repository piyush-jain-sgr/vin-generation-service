# import datetime
# import datetime
# from datetime import datetime
# #
# # now = datetime.now()
# # print(now)
#
# import csv
# def formAllLists():
#     with open('C:\\Users\\31817\\PycharmProjects\\vin-generation-service\\src\\file.csv', 'rt') as f:
#         unique_list = []
#         data = csv.reader(f)
#         data = list(data)
#         for x in data:
#             if x[0] and x[1] not in unique_list:
#                 if (str(x[0] != 'CanType' or str(x[1])) != 'Identifier'):
#                     unique_list.append([x[0], x[1]])
#         IdentifierList = [[] for _ in range(len(unique_list))]
#         for row in range(len(data)):
#             for i in range(len(unique_list)):
#                 if (str(data[row][0]) == unique_list[i][0] and str(data[row][1]) == unique_list[i][1]):
#                     IdentifierList[i].append([data[row][0], data[row][1], data[row][2], data[row][3]])
#         count = 0
#         for index in range(len(IdentifierList)):
#             if (str(IdentifierList[index][0][0]) == "GenericCAN"):
#                 count += 1
#         GenericIdentifierList = [[] for _ in range(count)]
#         count = 0
#         for index in range(len(IdentifierList)):
#             if (str(IdentifierList[index][0][0]) == "GenericCAN"):
#                 GenericIdentifierList[count].append(IdentifierList[index][0])
#                 count += 1
#         print("GenericCAN IdentifierList Length :{}".format(len(GenericIdentifierList)))
#
#         count = 0
#         for index in range(len(IdentifierList)):
#             if (str(IdentifierList[index][0][0]) == "ICCAN"):
#                 count += 1
#         ICIdentifierList = [[] for _ in range(count)]
#         count = 0
#         for index in range(len(IdentifierList)):
#             if (str(IdentifierList[index][0][0]) == "ICCAN"):
#                 ICIdentifierList[count].append(IdentifierList[index][0])
#                 count += 1
#         print("IC IdentifierList Length :{}".format(len(ICIdentifierList)))
#
#         count = 0
#         for index in range(len(IdentifierList)):
#             if (str(IdentifierList[index][0][0]) == "EmissionCAN"):
#                 count += 1
#         EmissionIdentifierList = [[] for _ in range(count)]
#         count = 0
#         for index in range(len(IdentifierList)):
#             if (str(IdentifierList[index][0][0]) == "EmissionCAN"):
#                 EmissionIdentifierList[count].append(IdentifierList[index][0])
#                 count += 1
#         print("EmissionCAN IdentifierList Length :{}".format(len(EmissionIdentifierList)))
#
#         count = 0
#         for index in range(len(IdentifierList)):
#             if (str(IdentifierList[index][0][0]) == "PrognosticCAN"):
#                 count += 1
#         PrognosticIdentifierList = [[] for _ in range(count)]
#         count = 0
#         for index in range(len(IdentifierList)):
#             if (str(IdentifierList[index][0][0]) == "PrognosticCAN"):
#                 PrognosticIdentifierList[count].append(IdentifierList[index][0])
#                 count += 1
#         print("Prognostic IdentifierList Length :{}".format(len(PrognosticIdentifierList)))
#         print(GenericIdentifierList)
#         print(ICIdentifierList)
#         print(EmissionIdentifierList)
#         print(PrognosticIdentifierList)
#
# formAllLists()

# class Person:
#   def printname1(self):
#     print("Hi Person")
#
# class Student(Person):
#   def printname(self):
#     print("Hi Student")
#
# class Parents(Student):
#     pass
#
#
# x = Parents()
# x.printname1()


x = 300
def myfunc1():
    def myfunc():
        global x
        x=199
        print(x)
    myfunc()
myfunc1()

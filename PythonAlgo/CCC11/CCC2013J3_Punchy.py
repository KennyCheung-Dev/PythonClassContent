# A = 0
# B = 0
# temp1 = 0
# temp2 = 0
# while (True):
#     s = input()
#     if s.split(" ")[0] == "1":
#         if s.split(" ")[1] == "A":
#             A = int(s.split(" ")[2])
#         if s.split(" ")[1] == "B":
#             B = int(s.split(" ")[2])
#     if s.split(" ")[0] == "2":
#         if s.split(" ")[1] == "A":
#             print(A)
#         if s.split(" ")[1] == "B":
#             print(B)
#     if s.split(" ")[0] == "3":
#         temp1 = A if s.split(" ")[1] == "A" else B
#         temp2 = A if s.split(" ")[2] == "A" else B
#         if s.split(" ")[1] == "A":
#             A = temp1 + temp2;
#         else:
#             B = temp1 + temp2;
#     if s.split(" ")[0] == "4":
#         temp1 = A if s.split(" ")[1] == "A" else B
#         temp2 = A if s.split(" ")[2] == "A" else B
#         if s.split(" ")[1] == "A":
#             A = temp1 * temp2
#         else:
#             B = temp1 * temp2
#     if s.split(" ")[0] == "5":
#         temp1 = A if s.split(" ")[1] == "A" else B
#         temp2 = A if s.split(" ")[2] == "A" else B
#         if s.split(" ")[1] == "A":
#             A = temp1 - temp2
#         else:
#             B = temp1 - temp2
#     if s.split(" ")[0] == "6":
#         temp1 = A if s.split(" ")[1] == "A" else B
#         temp2 = A if s.split(" ")[2] == "A" else B
#         if s.split(" ")[1] == "A":
#             A = int(temp1 // temp2)
#         else:
#             B = int(temp1 // temp2)
#     if s.split(" ")[0] == "7":
#         break;



A, B, temp1, temp2 = 0, 0, 0, 0
while (True):
    s = input()
    A = int(s.split(" ")[2]) if s.split(" ")[1] == "A" else B = int(s.split(" ")[2]) if s.split(" ")[0] == "1" else None
    print(A) if s.split(" ")[1] == "A" else print(B) if s.split(" ")[0] == "2" else None
    A = A if s.split(" ")[1] == "A" else B +  A if s.split(" ")[2] == "A" else B if s.split(" ")[1] == "A" else B = A if s.split(" ")[1] == "A" else B +  A if s.split(" ")[2] == "A" else B if s.split(" ")[0] == "3" else None
    A = A if s.split(" ")[1] == "A" else B * A if s.split(" ")[2] == "A" else B if s.split(" ")[1] == "A" else B = A if s.split(" ")[1] == "A" else B * A if s.split(" ")[2] == "A" else B if s.split(" ")[0] == "4" else None

    if s.split(" ")[0] == "5":
        temp1 = A if s.split(" ")[1] == "A" else B
        temp2 = A if s.split(" ")[2] == "A" else B
        if s.split(" ")[1] == "A":
            A = temp1 - temp2
        else:
            B = temp1 - temp2
    if s.split(" ")[0] == "6":
        temp1 = A if s.split(" ")[1] == "A" else B
        temp2 = A if s.split(" ")[2] == "A" else B
        if s.split(" ")[1] == "A":
            A = int(temp1 // temp2)
        else:
            B = int(temp1 // temp2)
    if s.split(" ")[0] == "7":
        break;

























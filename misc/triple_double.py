def TripleDouble(num1, num2):
    # Approach
    # 1. First convert the input into strings then separate each digit with the help of list comprehension
    # 2. Check the length : the first input1 must have len >=3 and second input2 must have len >= 2
    # 3. Run loop till len(input1) - 2 , since at most we need 3 elements, simultaneously check if all
    # .   the corresponding elements are same or not, if true then "".join and append to the triple var
    # 4. Run loop till len(input1) - 1 , since at most we need 2 elements, simultaneously check if all
    # .   the corresponding elements are same or not, if true then "".join and append to the triple var
    # 5. return 1 if element of double exist in element of triple (double[i] in triple[i])
    # 6. If none of the above code satisfies, it means that they are no triple double, hence return 0

    n1 = [str(i) for i in str(num1)]
    n2 = [str(i) for i in str(num2)]

    if len(n1) < 3 and len(n2) < 2:
        return 0

    triple = []
    double = []

    for i in range(len(n1) - 2):
        if n1[i] == n1[i+1] == n1[i+2]:
            triple.append("".join(n1[i:i+3]))

    for i in range(len(n2) - 1):
        if n2[i] == n2[i+1]:
            double.append("".join(n2[i:i+2]))

    print(triple)
    print(double)

    for i in range(len(triple)):
        if double[i] in triple[i]:
            return 1

    return 0

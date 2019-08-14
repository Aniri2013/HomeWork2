stanciya = {
    "A": '1 час.',
    "B": '2 часа.',
    "C": '3 часа.',
    "D": '4 часа.',
    "E": '5 часа.'
}
st = input("Введи станцию: ")
st = st.upper()
if st in stanciya:
    print(stanciya[st])

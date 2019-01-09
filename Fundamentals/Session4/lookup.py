teencode = {
    "eny": "Em nguoi yeu",
    "any": "Anh nguoi yeu",
    "lm": "Lam",
}
teencode_list = ["eny", "any", "lm"]
while True:
    print(*teencode_list)
    code = input("Enter code: ").lower()
    if code in teencode:
        ####
        print(teencode[code])
        need_update = input("Do you want to update (Y/N): ").upper()
        if need_update == "Y":
            new_trans = input("New translation: ")
            teencode[code] = new_trans
            print(teencode)       
    else:
        need_contribute = input("Code doesn't exists, contribute? (Y/N) ").upper()
        if need_contribute == "Y":
            trans = input("New translation? ")
            teencode[code] = trans
            teencode_list.append(code)
            print(teencode)

    
in_a = input()
in_p = int(input())
in_g = input()
in_a2 = input()
in_r = input()

dict_a = {"geen": 0, "zwak": 1, "goed doorhuilen": 2}
dict_g = {"slap": 0, "enige flexie": 1, "actieve beweging": 2}
dict_a2 = {"blauw": 0, "bleek": 0, "extremiteiten": 1, "roze": 2}
dict_r = {"geen": 0, "enige beweging": 1, "krachtig huilen": 2}

def calculate_answer(inp, dict):
    return dict[inp] if inp in dict else "ongeldige invoer"
ans_a = calculate_answer(in_a, dict_a)

ans_p = 0 if in_p == 0 else 1 if in_p < 100 else 2 if in_p >= 100 else "ongeldige invoer"
ans_g = calculate_answer(in_g, dict_g)
ans_a2 = calculate_answer(in_a2, dict_a2)
ans_r = calculate_answer(in_r, dict_r)

ans = "ongeldige invoer"
answers = [ans_a, ans_p, ans_g, ans_a2, ans_r]

if "ongeldige invoer" not in answers:
    ans = sum(answers)
    if ans < 4:
        ans = "alarm"

print(ans)
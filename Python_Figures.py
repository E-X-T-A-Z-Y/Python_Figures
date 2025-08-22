
def draw(n: int, fill_if, ch: str = "*"):

    ch = (ch or "*")[0]
    for i in range(n):
        line = "".join((ch + " ") if fill_if(i, j, n) else "  " for j in range(n))
        print(line)
    print()

def ask_int(prompt, lo=1, hi=50):
    while True:
        try:
            v = int(input(prompt))
            if lo <= v <= hi:
                return v
        except ValueError:
            pass
        print(f"Введіть ціле число в діапазоні [{lo}; {hi}]")

def ask_char(prompt):
    s = input(prompt).strip()
    return s[0] if s else "*"


# Рівень 1
def fig_a(i, j, n):
    return i >= j

def fig_b(i, j, n):
    return i <= j

def fig_i(i, j, n):
    return i <= (n - 1 - j)

def fig_k(i, j, n):
    return i >= (n - 1 - j)

# Рівень 2
def fig_v(i, j, n):
    return i >= j and i >= n - 1 - j

def fig_g(i, j, n):
    return i <= j and i <= n - 1 - j

def fig_zh(i, j, n):
    return j >= i and j >= n - 1 - i

def fig_z(i, j, n):
    return j <= i and j <= n - 1 - i

# Рівень 3
def fig_d(i, j, n):
    return (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j)

def fig_e(i, j, n):
    return (i <= j and i >= n - 1 - j) or (i >= j and i <= n - 1 - j)


MENU = {
    "1": ("а — нижній-лівий трикутник", fig_a),
    "2": ("б — верхній-правий трикутник", fig_b),
    "3": ("в — трикутник вниз ",   fig_v),
    "4": ("г — трикутник вгору ",  fig_g),
    "5": ("д — пісочний годинник",        fig_d),
    "6": ("е — метелик",         fig_e),
    "7": ("ж — стрілка вправо",           fig_zh),
    "8": ("з — стрілка вліво",            fig_z),
    "9": ("і — верхній-лівий (побічна)",  fig_i),
    "10":("к — нижній-правий (побічна)",  fig_k),
}

def main():
    while True:
        print("\n=== МЕНЮ ФІГУР ===")
        for key in sorted(MENU, key=lambda x: int(x)):
            print(f"{key}. {MENU[key][0]}")
        print("0. Вихід")

        choice = input("Ваш вибір: ").strip()
        if choice == "0":
            print("Бувай!")
            break
        if choice not in MENU:
            print("Невірний пункт меню.")
            continue

        n = ask_int("Розмір n (рекомендовано 9 або 11): ", lo=3, hi=99)
        ch = ask_char("Символ заповнення (Enter = *): ")
        _, predicate = MENU[choice]
        draw(n, predicate, ch)

if __name__ == "__main__":
    main()

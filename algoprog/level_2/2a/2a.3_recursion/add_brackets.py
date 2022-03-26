def add_brackets(s):
    if len(s) <= 2:
        return s
    else:
        return s[0] + "(" + add_brackets(s[1:-1]) + ")" + s[-1]


def main():
    str_ = input()

    new_str = add_brackets(str_)

    print(new_str)

    # assert add_brackets("card") == "c(ar)d", f"The result is {add_brackets('card')}"
    # assert add_brackets("example") == "e(x(a(m)p)l)e", f"The result is {add_brackets('example')}"
    # assert add_brackets(
    #     "LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO") == \
    #        "L(I(t(B(e(o(F(L(c(S(G(B(O(F(Q(x(M(H(o(I)u)D)D)W)c)q)c)V)g)k)c)R)o)A)e)o)c)X)O", \
    #     f"The result is {add_brackets('LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO')}"


if __name__ == '__main__':
    main()

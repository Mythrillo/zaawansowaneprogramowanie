def deterministic_miller_rabin_primality_test(n: int) -> bool:
    # Since our goal is to test only n < 2^64 we can use a deterministic miller-rabin test.
    # Bases are taken from http://miller-rabin.appspot.com/
    if n == 1:
        return False
    if n % 2 == 0 and n != 2:
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    bases = _get_bases(n)
    return not any(_check_base(n, d, s, base) for base in bases)


def _check_base(n: int, d: int, s: int, base: int) -> bool:
    if pow(base, d, n) == 1:
        return False
    for i in range(s):
        if pow(2, 2**i * d, n) == n - 1:
            return False
    return True


def _get_bases(n: int) -> list[int]:
    if n < 341531:
        return [9345883071009581737]
    elif n < 1050535501:
        return [336781006125, 9639812373923155]
    elif n < 350269456337:
        return [4230279247111683200, 14694767155120705706, 16641139526367750375]
    elif n < 55245642489451:
        return [2, 141889084524735, 1199124725622454117, 11096072698276303650]
    elif n < 7999252175582851:
        return [
            2,
            4130806001517,
            149795463772692060,
            186635894390467037,
            3967304179347715805,
        ]
    elif n < 585226005592931977:
        return [
            2,
            123635709730000,
            9233062284813009,
            43835965440333360,
            761179012939631437,
            1263739024124850375,
        ]
    return [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

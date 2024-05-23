class Polynomial:
    def __init__(self, *terms: int):
        self._terms = tuple(terms)

    def __str__(self):
        out = str(self._terms[0]) if self._terms and self._terms[0] else ""
        for p, term in enumerate(self._terms[1:], 1):
            if term == 0:
                continue
            if out:
                out += " + " if term > 0 else " - "
            if abs(term) != 1:
                out += str(abs(term))
            out += "x"
            if p > 1:
                out += f"^{p}"
        return out

    def __mul__(self, other: 'Polynomial'):
        result_terms = [0] * (len(self._terms) + len(other._terms) - 1)
        for i, term1 in enumerate(self._terms):
            for j, term2 in enumerate(other._terms):
                result_terms[i + j] += term1 * term2
        return Polynomial(*result_terms)


print(f'({Polynomial(1, 2, 3)}) * ({Polynomial(4, 5, 6)}) = {Polynomial(1, 2, 3) * Polynomial(4, 5, 6)}')
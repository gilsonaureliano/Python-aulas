def fatorial(n , show= False):
    """
    <<<Calcula o fatorual de um numero>>
    :param n: ' Numero a ser fatorado'
    :param show: 'Chave (OPCIONAL) para fazer print do calculo
    :return: 'Retorno da fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', 'x' if c != 1 else '=', end=' ')
    return f


r = fatorial(5, show=True)
print(r)

help(fatorial)
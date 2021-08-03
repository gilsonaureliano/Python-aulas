def notas(*n, sit=False):
    """
    'Dicionario de notas'
    :param n: 'Notas dos alunos'
    :param sit: 'Situação final"
    :return: 'Total, maior, menor, situação(op)'
    """
    global men, med
    dic = {}
    dic['total'] = len(n)
    mai = 0
    total = 0
    for c, v in enumerate(n):
        if n[c] > mai:
            mai = v
        if c == 0:
            men = v
        if c > 1:
            if v < men:
                men = v
        total += v
        med = total / len(n)
    dic['maior'] = mai
    dic['menor'] = men
    dic['media'] = med
    if sit:
        if med <= 5:
            dic['situação'] = 'RUIM'
        elif 5 < med < 7:
            dic['situação'] = 'REGULAR'
        else:
            dic['situação'] = 'BOA'
    return dic


# programa principal
resp = notas(6, 7, 5, 9, 9, 9, sit=True)
print(resp)

help(notas)

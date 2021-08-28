class Knn():

    def __init__(self, k, data):
        self.k = k
        self.data = data

    def calcularDistancia(self, cartAtual, cartVizinho):
        """
        Calcula a distância entre a carteira de investimentos em questão e outra carteira de investimentos
        """
        distancia = 0
        for i in range(len(cartAtual)):
            distancia += (cartAtual[i] - cartVizinho[i])**2
        return distancia**.5

    def encontrarMaisProximos(self, pessoa):
        """
        Após os primeiros 'k' investidores, a cada novo investidor, mantém sempre os 'k' mais próximos excluindo o maior valor
        """
        listProximos = []
        for v in range(len(self.data)):
            listProximos.append((self.data[v][1], self.calcularDistancia(pessoa[2], self.data[v][2])))
            if v >= self.k:
                listPerfisDistancias = list(zip(*listProximos))
                idxMaior = listPerfisDistancias[1].index(max(listPerfisDistancias[1]))
                listProximos.pop(idxMaior)
        return listProximos

    def definirPerfil(self, listPerfisProximos):
        """
        Faz a contagem para definir qual o perfil do investidor
        """
        dicTotais = {
            'Conservador': 0,
            'Moderado': 0,
            'Agressivo': 0
        }
        for perfil in listPerfisProximos:
            if perfil[0] == 'Conservador':
                dicTotais['Conservador'] += 1
            elif perfil[0] == 'Moderado':
                dicTotais['Moderado'] += 1
            else:
                dicTotais['Agressivo'] += 1
        totais = [dicTotais.get('Conservador'), dicTotais.get('Moderado'), dicTotais.get('Agressivo')]
        maior = max(totais)
        if (maior == dicTotais.get('Conservador')):
            return 'Conservador'
        elif (maior == dicTotais.get('Moderado')):
            return 'Moderado'
        else:
            return 'Agressivo'
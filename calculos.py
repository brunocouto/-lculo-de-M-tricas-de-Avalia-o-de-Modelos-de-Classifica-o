def calcular_metricas(VP, VN, FP, FN):
    # Acurácia
    acuracia = (VP + VN) / (VP + VN + FP + FN)
    
    # Precisão
    precisao = VP / (VP + FP) if (VP + FP) != 0 else 0
    
    # Sensibilidade
    sensibilidade = VP / (VP + FN) if (VP + FN) != 0 else 0
    
    # Especificidade
    especificidade = VN / (VN + FP) if (VN + FP) != 0 else 0
    
    # F-Score
    if precisao + sensibilidade != 0:
        f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)
    else:
        f_score = 0
    
    # Exibindo os resultados
    return {
        "Acurácia": acuracia,
        "Precisão": precisao,
        "Sensibilidade": sensibilidade,
        "Especificidade": especificidade,
        "F-Score": f_score
    }

# Valores arbitrários para a matriz de confusão
VP, VN, FP, FN = 50, 35, 5, 10

# Calculando as métricas
metricas = calcular_metricas(VP, VN, FP, FN)

# Exibindo as métricas
for nome, valor in metricas.items():
    print(f"{nome}: {valor:.2f}")

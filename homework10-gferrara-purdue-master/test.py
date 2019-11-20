colors = ['b', 'g', 'r', 'c', 'm']
markers = ['+', 'x', 'd', 's', '.']

x_data.sort()
for n in range(len(degrees)):
    y_n = list()
    y_n_mse = 0
    for point in x_data:
        sum = 0
        for i in range(len(paramFits[n])):
            count = paramFits[n][i] * (point ** (len(paramFits[n]) - (i + 1)))
            sum += count
        y_n.append(sum)
    for i in range(len(Y)):
        dif = (y_n[i] - Y[i]) ** 2
        y_n_mse += dif
        # y_1_msd.append(dif)
    print(f'MSE Degree {degrees[n]}: {y_n_mse}')
    for i in range(n + 1):
        print(f'x^{degrees[n] - i}*{paramFits[n][i]} + ', end='')
    print(paramFits[n][-1])
    plt.plot(x_data, y_n, color=colors[n], marker=markers[n], label=f'Degree {degrees[n]}')
plt.legend()
plt.show()
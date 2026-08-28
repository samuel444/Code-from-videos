import math


def RoR(bettings, bankroll):
    probabilities = [0.01225,0.02161,0.03802,0.06725,0.122196,0.458485,0.117709,0.06483,0.0367,0.02094,0.01184,0.00644,0.00355,0.00189,0.00096,0.00047]
    expected = [-0.03179,-0.02545,-0.01988,-0.01446,-0.00806,-0.00114,0.00609,0.00839,0.01280,0.02105,0.02815,0.03756,0.04446,0.05191,0.05971,0.06603]
    expectations = []
    variance = []
    for i in range(len(probabilities)):
        expectations.append(probabilities[i]*expected[i]*bettings[i])
    expectations = sum(expectations)
    variances = []
    V0 = 1.35
    for i in range(len(probabilities)):
        variances.append(probabilities[i]*(V0 * (bettings[i]**2) + ((expected[i] * bettings[i] - expectations)**2)))
    variance = sum(variances)
    inside = (-2 * expectations * bankroll)/variance
    risk = math.exp(inside)
    if risk > 1:
        risk = 1
    return str(int(10000*risk)/100), str(int(expectations*20000)/100)

def findBet(money):
    tableBudget = [(5,100,1),(10,500,5),(25,9995,10),(50,2000,25),(100,5000,50),(250,99950,100),(500,25000,500)]
    if money > 1000000:
        table = 6
    elif money > 500000:
        table = 5
    elif money > 200000:
        table = 4
    elif money > 100000:
        table = 3
    elif money > 50000:
        table = 2
    elif money > 20000:
        table = 1
    else:
        table = 0
    stop = False
    text = [str(money),str(tableBudget[table][0]),str(tableBudget[table][0]),str(tableBudget[table][0]),str(tableBudget[table][0]),str(tableBudget[table][0]),str(tableBudget[table][0]),str(tableBudget[table][0]),str(2*tableBudget[table][0]),str(2*tableBudget[table][0]),str(2*tableBudget[table][0]),str(2*tableBudget[table][0]),str(2*tableBudget[table][0]),str(2*tableBudget[table][0]),str(2*tableBudget[table][0]),str(2*tableBudget[table][0]),str(2*tableBudget[table][0])]
    true = 7
    money_value = tableBudget[table][0]
    values = [0 for j in range(tableBudget[table][0],tableBudget[table][1]+tableBudget[table][2],tableBudget[table][2])]
    while not stop:
        text[true] = str(money_value)
        if money_value > tableBudget[table][1]:
            reversing = list(reversed(values))
            location = reversing.index(min(values))
            location = (len(reversing)-1-location)
            text[true] = str(tableBudget[table][0] + tableBudget[table][2]*location)
            values = [0 for j in range(tableBudget[table][0],tableBudget[table][1]+tableBudget[table][2],tableBudget[table][2])]
            true += 1
            money_value = tableBudget[table][0]

            if true > 16:
                true = 7
                stop = True
            
        try:
            bankroll = int(text[0])
            bettings = [int(text[j]) for j in range(1,17)]
            risk,expectation = RoR(bettings,bankroll)
        except Exception:
            risk = 'NA'
            expectation = 'NA'


        if not stop:
            find = ((money_value-tableBudget[table][0])//tableBudget[table][2])
            values[find] = float(risk)
            money_value += tableBudget[table][2]

    text = text[1:]
    for i in range(20):
        text.append(text[15])
    print ('Your risk of ruin is ' + str(risk) + '%')
    print ('Making an expected $' + expectation + ' per hour')
    return text

money = 20000
print("For a starting bankroll: $" + str(money))
results = findBet(money)
print ('Using the bet spread:')
print ('True 0 or less: $' + results[0])
for i in range(6,11):   
    print ('True '+str(i-5)+ ': $' + results[i])
print ('True 6+: $'+ results[11])





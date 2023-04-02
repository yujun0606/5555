population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]
population1 = population[1]
print(f"서울인구: {population1}")
population3 =  population[3]
population2 = population[-1]
print(f"인천인구: {population2}")
population.remove(9765)
population.remove(3441)
population.remove(2954)
print(population)

population4 = population1 + population3  + population2
print(f"인구의 합: {population4}")

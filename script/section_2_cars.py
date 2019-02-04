import numpy as np
import pandas as pd

def initiate_position(N, M):
    N_circle = np.zeros(N)
    for i in range(M):
        N_circle[i] = 1
    return N_circle

#find movable location:
def find_movable_cars(N_circle, N):
    movable_car_index = []
    for i in range(N): #i is the locatio of the cars
        #cannot be last i
        if i != N-1:
            if N_circle[i] == 1 and N_circle[i+1] == 0:
                #movable
                movable_car_index.append((i, i+1))
        else: #when i is the last loc
            if N_circle[i] == 1 and N_circle[0] == 0:
                movable_car_index.append((i, 0))
    return movable_car_index

def move_cars(N_circle, movable_cars):
    move_car = movable_cars[np.random.choice(range(len(movable_cars)))]
    N_circle[move_car[0]] = 0
    N_circle[move_car[1]] = 1
    return N_circle

def main():
    

    N = int(input('give N: '))
    M = int(input('give M: '))
    T = int(input('give T: '))

    repeat = 999999
    As = []
    Ss = []
    for kkkkk in range(repeat):
        car_circle = initiate_position(N, M)
        t = T
        while t:
            movable_cars = find_movable_cars(car_circle, N)
            car_circle = move_cars(car_circle, movable_cars)
            t -= 1
        A = np.dot(np.array(range(N)),car_circle)/M
        S = np.sqrt(np.dot(np.square(np.array(range(N))), car_circle)/M - np.square(A))
        As.append(A)
        Ss.append(S)

    df = pd.DataFrame(index=range(len(As)), columns=['A','S'], data={'A':As,'S':Ss})
    print('A mean {}'.format(df.A.mean()))
    print('S mean {}'.format(df.S.mean()))
    print('A std {}'.format(df.A.std()))
    print('S std {}'.format(df.A.std()))
    
if __name__ == '__main__':
    main()
 
import random
from tqdm import tqdm

N_TRIALS = 10000000
TARGET_SUM = 7

def run_exp():
    dice_1 = random.choice([1, 2, 3, 4, 5, 6])
    dice_2 = random.choice([1, 2, 3, 4, 5, 6])
    return dice_1 + dice_2

def main():
    n_events = 0
    for i in tqdm(range(N_TRIALS)):
        dice_total = run_exp()
        if(dice_total == TARGET_SUM):
            n_events += 1
    pr_e = n_events / N_TRIALS
    print(f'After {N_TRIALS} trials')
    print('P(E) ~ ', pr_e)

if __name__ == '__main__':
    main()

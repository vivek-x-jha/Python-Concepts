import numpy as np
import matplotlib.pyplot as plt

"""Each rng produced by .rand() is pseudo-random i.e. random w.r.t. a given "seed""""
np.random.seed(123)

all_walks = []
for i in range(5):

    random_walk = [0]

    # Rule1: Have 100 steps to take
    for x in range(100):

        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        # More rules:
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1, 7)

        # Implement "clumsiness" rule
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

np_aw = np.array(all_walks)
last_col = np.transpose(np_aw[:, -1])

plt.plot(np.transpose(np_aw))
plt.show()

plt.hist(last_col, bins=20)
plt.show()

"""Calculate odds of landing on final step"""
final_step = 60
odds = np.mean(last_col >= final_step)
print(f'Odds of being atleast {final_step} steps: {odds:.1%}')

import numpy as np
import random

# Environment parameters
rows = 5      # number of steps to reach goal (downward)
cols = 3      # positions: 0=left, 1=middle, 2=right
actions = ["right", "left", "right"]  # fixed sequence

Q = np.zeros((rows, cols))

# Training parameters
episodes = 1000
alpha = 0.8
gamma = 0.9

def is_car_at(row, col):
    return random.random() < 0.2  # 20% chance of obstacle

# Train the agent
for episode in range(episodes):
    row, col = 0, 1  # Start at (0, middle)
    step_index = 0
    done = False

    while not done:
        action = actions[step_index % len(actions)]  # right → left → right...

       
        if action == "left":
            col = max(0, col - 1)
        elif action == "right":
            col = min(cols - 1, col + 1)

        # Always move forward after each horizontal move
        row = min(rows - 1, row + 1)

        # Check result of move
        if is_car_at(row, col):
            reward = -10
            done = True
        elif row == rows - 1:
            reward = 10
            done = True
        else:
            reward = -1

        # Q-learning update (useful for evaluating which states are better)
        if not done:
            Q[row, col] += alpha * (reward + gamma * np.max(Q[row, col]) - Q[row, col])
        else:
            Q[row, col] += alpha * (reward - Q[row, col])

        step_index += 1

# Test the agent
print("\n🚶 Agent following fixed action pattern (right → left → right):")
row, col = 0, 1
step_index = 0
path = [(row, col)]

while row < rows - 1:
    action = actions[step_index % len(actions)]
    if action == "left":
        col = max(0, col - 1)
    elif action == "right":
        col = min(cols - 1, col + 1)
    row = min(rows - 1, row + 1)
    path.append((row, col))
    step_index += 1

for i, pos in enumerate(path):
    print(f"Step {i}: Position = {pos}")

print(f"\n✅ Reached goal in {len(path)-1} steps.")

# Show Q-values learned
print("\n📊 Q-values (usefulness of states):")
print(np.round(Q, 2))

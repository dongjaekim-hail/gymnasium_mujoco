import gymnasium as gym

env = gym.make('Ant-v4')

env.reset()

for _ in range(1):
    obs, info = env.reset()
    done, truncated = False, False

    for _ in range(1000):
        action = env.action_space.sample()
        obs, reward, done, truncated, info = env.step(action)

        env.render()
from board import *
from dqn import DeepQNetwork

env = Board(7,7)



RL = DeepQNetwork(n_actions=10,
                  n_features=49,
                  learning_rate=0.01, e_greedy=0.9,
                  replace_target_iter=100, memory_size=2000,
                  e_greedy_increment=0.001, output_graph=True)

total_steps = 0

for i_episode in range(200):

    observation = env.reset()
    ep_r = 0
    while True:
        # env.render()

        action = RL.choose_action(observation)

        observation_, reward, done = env.step(action)

        RL.store_transition(observation, action, reward, observation_)

        ep_r += reward
        if total_steps > 1000:
            RL.learn()

        if done:
            print('episode: ', i_episode,
                  'ep_r: ', round(ep_r, 2),
                  ' epsilon: ', round(RL.epsilon, 2))
            break

        observation = observation_
        total_steps += 1

RL.plot_cost()

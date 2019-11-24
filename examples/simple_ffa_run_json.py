'''An example to show how to set up an pommerman game programmatically'''
import pommerman
from pommerman import agents
import sys
sys.path.append("../pommerman")
import fight

def main():
    '''Simple function to bootstrap a game.
       
       Use this as an example to set up your training env.
    '''
    # Print all possible environments in the Pommerman registry
    print(pommerman.REGISTRY)

    # Generate a json every 5 episodes
    json_check = 5 

    # Create a set of agents (exactly four)
    agent_list = [
            agents.SimpleAgent(),
            agents.RandomAgent(),
            agents.SimpleAgent(),
            agents.RandomAgent(),
            ]
    deep_agents = 'test::agents.SimpleAgent,test::agents.RandomAgent,test::agents.RandomAgent,test::agents.SimpleAgent'
        #agents.DockerAgent("multiagentlearning/hakozakijunctions", port=12345),
        #agents.DockerAgent("multiagentlearning/eisenach", port=12345),
        #agents.DockerAgent("multiagentlearning/skynet955", port=12345),
    
    # Make the "Free-For-All" environment using the agent list
    config = 'PommeFFACompetition-v0'
    #config = 'PommeTeamCompetition-v1'
    env = pommerman.make(config, agent_list)

    # Run the episodes just like OpenAI Gym
    for i_episode in range(20):
        if i_episode % json_check == 0:
            fight.run(config, deep_agents, record_json_dir = "test_json" + str(i_episode)) # GIVES ME ERROR DURING env.save_json
        else:
            state = env.reset()
            done = False
            while not done:
                actions = env.act(state)
                state, reward, done, info = env.step(actions)
    
            print('Episode {} finished'.format(i_episode))
            print("Final Result: ", info)

    env.close()


if __name__ == '__main__':
    main()

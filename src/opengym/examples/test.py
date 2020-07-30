import argparse
from ns3gym import ns3env

__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2018, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "gawlowicz@tkn.tu-berlin.de"


parser = argparse.ArgumentParser(description='Start simulation script on/off')
parser.add_argument('--start',
                    type=int,
                    default=1,
                    help='Start simulation script True/False, Default: True')
args = parser.parse_args()
startSim = bool(args.start)

print("startSim: ", startSim)


stepTime = 0.5  # seconds
env = ns3env.Ns3Env(stepTime=stepTime, startSim=startSim)
env.reset()

ob_space = env.observation_space
ac_space = env.action_space
print("Observation space: ", ob_space,  ob_space.dtype)
print("Action space: ", ac_space, ac_space.dtype)

stepIdx = 0

try:
    while True:
        stepIdx += 1
        print("Step: ", stepIdx)

        action = env.action_space.sample()
        print("---action: ", action)
        obs, reward, done, info = env.step(action)
        print("---obs, reward, done, info: ", obs, reward, done, info)

        if done:
            break

except KeyboardInterrupt:
    print("Ctrl-C -> Exit")
finally:
    pass

print("Done")
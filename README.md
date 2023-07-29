# BAISIK

Basic Artificial Intelligence Specializing in Kickboxing, or BAISIK, is a Python AI for the
FightingICE platform. It is a simple blind AI that only uses the audio data from the game as
input.

The strategy of BAISIK is to kick the opponent as much as possible. It will always try to
kick the opponent, and if it is not possible, it will try to move closer to the opponent.

## File Description

- `DisplayInfo.py` is an example AI that utilizes screen data as input.
- `BAISIK.py` is the main AI that utilizes audio data as input.
- `Main_PyAIvsPyAI.py` is the script to run two instances of the Python AI and set up the game. This is when both AI are implemented using Python
- `Main_SinglePyAI.py` is the script to run a single instance of the Python AI, e.g. when the opposing AI is not implemented using Python.

## Instruction

- First, install our interface on implementing python AI using `pip`.

```bash
pip install pyftg
pip install numpy
pip install --upgrade google-api-python-client
```

## Instruction on using Main_PyAIvsPyAI.py

- Boot DareFightingICE with option `--grpc-auto`.
- If both of AI are implemented in Python, modify lines 11 to 15 of `Main_PyAIvsPyAI.py`.
- The following example shows how to use BAISIK as player 1 and DisplayInfo as player 2.

```python
agent1 = BAISIK()
agent2 = DisplayInfo()
gateway.register_ai("BAISIK", agent1)
gateway.register_ai("DisplayInfo", agent2)
gateway.run_game([character, character], ["BAISIK", "DisplayInfo"], game_num)
```

- Execute `Main_PyAIvsPyAI.py` to connect to the DareFightingICE platform where `port` is the exposed port of DareFightingICE (optional).

```bash
python Main_PyAIvsPyAI.py --port {port}
```

## Instruction on using Main_SinglePyAI.py

- Boot DareFightingICE with the option `--grpc`.
- To run a single instance of the Python AI, refer to `Main_SinglePyAI.py`.
- Execute `Main_SinglePyAI.py`, the following example shows how to use BAISIK as player 1 and not select anything for player 2.

```bash
python Main_SinglePyAI.py --a1 BAISIK
```

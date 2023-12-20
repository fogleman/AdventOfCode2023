from collections import defaultdict
import fileinput
import re

modules = {}
queue = []

class Module:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.sources = set()
        self.sent = defaultdict(int)
    def send(self, pulse):
        self.sent[pulse] += len(self.destinations)
        for name in self.destinations:
            if name not in modules:
                continue
            queue.append((modules[name], self.name, pulse))

class Broadcaster(Module):
    def receive(self, source, pulse):
        self.send(pulse)

class FlipFlop(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.state = False
    def receive(self, source, pulse):
        if not pulse:
            self.state = not self.state
            self.send(self.state)

class Conjunction(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.state = defaultdict(bool)
        self.lo = False
    def value(self):
        result = sum(self.state.values()) != len(self.sources)
        if not result:
            self.lo = True
        return result
    def receive(self, source, pulse):
        self.state[source] = pulse
        self.send(self.value())

MODULE_TYPES = {'%': FlipFlop, '&': Conjunction}

for line in fileinput.input():
    names = re.findall(r'\w+', line)
    cls = MODULE_TYPES.get(line[0], Broadcaster)
    for name in names[1:]:
        print('%s -> %s;' % (names[0], name))
    modules[names[0]] = cls(names[0], names[1:])

for module in modules.values():
    for name in module.destinations:
        if name not in modules:
            continue
        modules[name].sources.add(module.name)

names = ['qz','lx','db','sd']
ms = [modules[x] for x in names]
prev = [0] * len(ms)
ds = [0] * len(ms)
def check(index):
    for i, x in enumerate(ms):
        if x.lo:
            ds[i] = index - prev[i]
            prev[i] = index
        x.lo = False
    print(index, ds)
    # 4001*4027*3929*3769

def process_queue():
    while queue:
        obj, source, pulse = queue.pop(0)
        if obj.name == 'rx' and pulse == False:
            raise
        obj.receive(source, pulse)

def press_button():
    modules['broadcaster'].sent[False] += 1
    modules['broadcaster'].receive(None, False)
    process_queue()

def counts():
    sent = defaultdict(int)
    for module in modules.values():
        for k, v in module.sent.items():
            sent[k] += v
    return sent[False], sent[True]

memo = {}
for i in range(1000000000):
    press_button()
    check(i)

lo, hi = counts()
print(lo * hi)

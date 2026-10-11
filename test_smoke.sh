#!/bin/sh
# Plays 20 random paths through the game and checks each reaches an ending ("play again" prompt).
ok=0
for s in $(seq 1 20); do
  out=$(python3 -c "import random;random.seed($s);print('\n'.join(random.choice('abc') for _ in range(80)))" | sed '$a no' | timeout 5 python3 lantern_lighthouse.py 2>&1)
  echo "$out" | grep -qi "play again" && ok=$((ok+1))
done
echo "$ok/20 random playthroughs reached an ending"
[ "$ok" -eq 20 ]

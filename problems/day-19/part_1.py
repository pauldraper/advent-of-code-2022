#!/usr/bin/env python3
import functools
import re
import sys

blueprint = re.compile("(Blueprint \d+|[a-zA-Z.: ])+")
total = 0
for i, line in enumerate(sys.stdin, 1):
    print(i)
    ore_ore, cla_ore, obs_ore, obs_cla, geo_ore, geo_obs = map(
        int, blueprint.sub(" ", line).strip().split(" ")
    )

    @functools.cache
    def best(ore, cla, obs, ore_rob, cla_rob, obs_rob, time):
        if time == 0:
            return 0
        if geo_ore <= ore and geo_obs <= obs:
            return (time - 1) + best(
                ore + ore_rob - geo_ore,
                cla + cla_rob,
                obs + obs_rob - geo_obs,
                ore_rob,
                cla_rob,
                obs_rob,
                time - 1,
            )
        result = 0
        can_build = False
        if ore_ore <= ore:
            can_build = True
            result = max(
                result,
                best(
                    ore + ore_rob - ore_ore,
                    cla + cla_rob,
                    obs + obs_rob,
                    ore_rob + 1,
                    cla_rob,
                    obs_rob,
                    time - 1,
                ),
            )
        if cla_ore <= ore:
            can_build = True
            result = max(
                result,
                best(
                    ore + ore_rob - cla_ore,
                    cla + cla_rob,
                    obs + obs_rob,
                    ore_rob,
                    cla_rob + 1,
                    obs_rob,
                    time - 1,
                ),
            )
        if obs_ore <= ore and obs_cla <= cla:
            can_build = True
            result = max(
                result,
                best(
                    ore + ore_rob - obs_ore,
                    cla + cla_rob - obs_cla,
                    obs + obs_rob,
                    ore_rob,
                    cla_rob,
                    obs_rob + 1,
                    time - 1,
                ),
            )
        if ore + ore_rob - ore_ore < max(cla_ore, obs_ore, geo_ore) and ore < ore_ore:
            result = max(
                result,
                best(
                    ore + ore_rob,
                    cla + cla_rob,
                    obs + obs_rob,
                    ore_rob,
                    cla_rob,
                    obs_rob,
                    time - 1,
                ),
            )
        return result

    total += i * best(0, 0, 0, 1, 0, 0, 24)
print(total)

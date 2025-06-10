# 🗺LLM-Driven Text Adventure Agent

This project implements a rule-based and LLM-assisted agent capable of navigating a structured text adventure environment. 
The game world is defined via a JSON configuration, enabling rapid prototyping and interaction via terminal.
The agent should be able to collect items, unlock doors, avoid traps, and pursue a successful path through decision-making logic.

---

## 📍World Map (ASCII)

                             +----------------------+
                             |   treasure_room      |
                             | (GOOD ENDING)        |
                             +----------+-----------+
                                        ↑ use key
                             +----------+-----------+
                             |    stone_door        |
                             +----------+-----------+
                                        ↑ go east
                             |     dark_tunnel      |
             +---------------+----------+-----------+----------------+
             |                          ↑                         ↑   |
             |                      go north                 go west |
     +-------+--------+       +-------------+             +----------+---------+
     |  side_chamber  |       |             |             |   cave_entrance    |
     +-------+--------+       |             |             +----------+---------+
             ↓ go west        |             |                         ↑
        +----+----+           |             |                    go north
        | trap_room|          |             |                         ↑
        +----------+          |             |                         |
                              |             |                         |
                              |             |                         |
                              |             |                         |
                              ↓             ↓                         ↓
                         (fallback)    (game over)            +---------------+
                                          ↖ go forward        |  forest_path  |
                                                              +-------+-------+
                                                                      ↓ go east
                                                             +--------+--------+
                                                             |    ruined_hut   |
                                                             +--------+--------+
                                                                      ↓ take key
                                                             +--------+--------+
                                                             |ruined_hut_key...|
                                                             +-----------------+
